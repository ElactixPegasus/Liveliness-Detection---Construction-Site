from email.mime import image
from operator import le
from tkinter import Frame
from traceback import print_tb
from unicodedata import name
import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

path = 'Images_of_students'
image = [] 
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    image.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode  = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('Attendancedata.csv','r+') as f:
        DataList = f.readlines()
        nameList = []
        print(DataList)
        for line in DataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')




encodeListKnown = findEncodings(image)
# print(len(encodeListKnown))
print("Encoding Complete")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgs = cv2.resize(img,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgs)
    encodeCurFrame  = face_recognition.face_encodings(imgs,facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDist = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDist)
        matchIndex= np.argmin(faceDist)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img, name,(x1+6,y2-6),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2)
            markAttendance(name)

    cv2.imshow('Webcam',img)
    cv2.waitKey(1)



# face_loc = face_recognition.face_locations(img)[0]
# img_encoder  = face_recognition.face_encodings(img)[0]
# cv2.rectangle(img,(face_loc[3],face_loc[0]),(face_loc[1],face_loc[2]),(255,0,255),2)

# face_loc_test = face_recognition.face_locations(imgTest)[0]
# img_encoder_Test  = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest,(face_loc_test[3],face_loc_test[0]),(face_loc_test[1],face_loc_test[2]),(255,0,255),2)

# results =  face_recognition.compare_faces([img_encoder_Test],img_encoder)
# facedis = face_recognition.face_distance([img_encoder],img_encoder_Test)


# img = face_recognition.load_image_file("Images_of_students/elontest.jpeg")
# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# imgTest = face_recognition.load_image_file('Images_of_students/elon1.jpg')
# imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
