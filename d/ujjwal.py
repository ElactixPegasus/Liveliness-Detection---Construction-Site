from tkinter import Frame
from unicodedata import name
import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime


img = face_recognition.load_image_file("Images_of_students/elontest.jpeg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Images_of_students/elon1.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

face_loc = face_recognition.face_locations(img)[0]
img_encoder  = face_recognition.face_encodings(img)[0]
cv2.rectangle(img,(face_loc[3],face_loc[0]),(face_loc[1],face_loc[2]),(255,0,255),2)

face_loc_test = face_recognition.face_locations(imgTest)[0]
img_encoder_Test  = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(face_loc_test[3],face_loc_test[0]),(face_loc_test[1],face_loc_test[2]),(255,0,255),2)

results =  face_recognition.compare_faces([img_encoder_Test],img_encoder)
facedis = face_recognition.face_distance([img_encoder],img_encoder_Test)

print(facedis)

cv2.putText(imgTest,f'{results}{round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('ronaldo',img)
cv2.imshow('ronaldo', imgTest)


cv2.waitKey(0)




# video_capture = cv2.VideoCapture(0)

# student1_image = face_recognition.load_image_file("Images_of_students/student1.jpg")
# student1_encoding = face_recognition.face_encodings(student1_image)[0]

# student2_image = face_recognition.load_image_file('Images_of_students/student2.jpg')
# student2_encoding = face_recognition.face_encodings(student2_image)[0]

# student3_image = face_recognition.load_image_file('Images_of_students/student3.jpg')
# student3_encoding = face_recognition.face_encodings(student3_image)[0]

# known_face_encoding = [
#     student1_encoding,
#     student2_encoding,
#     student3_encoding
# ]

# known_face_names = [
#     "City",
#     "Pogba",
#     "Ronaldo"
# ]

# students = known_face_names.copy()

# face_location = []
# face_encoding = []
# face_name = []
# s = True

# now = datetime.now()
# current_date = now.strftime("%Y-%m-%d")

# f = open(current_date +'.csv','w+',newline='')
# lnwriter = csv.writer(f)

# while True:
#     _,frame = video_capture.read()
#     small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
#     rgb_small_frame = small_frame[:,:,::-1]
#     if s:
#         face_location = face_recognition.face_locations(rgb_small_frame)
#         face_encoding = face_recognition.face_encodings(rgb_small_frame,face_location)
#         face_names = []
#         for face_encoding in face_encoding:
#             matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
#             name=''
#             face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
#             best_match_index = np.argmin(face_distance)
#             if matches[best_match_index]:
#                 name = known_face_names[best_match_index]
#             face_name.append(name)
#             if name in known_face_names:
#                 if name in students:
#                     students.remove(name)
#                     print(students)
#                     current_time = now.strftime("%H-%M-%S")
#                     lnwriter.writerow([name,current_time])
#     cv2.imshow("attendance system",frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# video_capture.release()
# cv2.destroyAllWindows()
# f.close()