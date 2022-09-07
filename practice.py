# class BST:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def append_node(self,data):
#         if self.data == data:
#             return ""
#         else:
#             if data < self.data:
#                 if self.left:
#                     self.left.append_node(data)
#                 else:
#                     self.left = BST(data)
#             elif data > self.data:
#                 if self.right:
#                     self.right.append_node(data)
#                 else:
#                     self.right = BST(data)
#     def print_BST(self):
#         element = []
#         if self.left:
#             element += self.left.print_BST()
#         element.append(self.data)
#         if self.right:
#             element += self.right.print_BST()
#         return element

# obj_BST = BST(15)
# obj_BST.append_node(4)
# obj_BST.append_node(8)
# obj_BST.append_node(3)
# obj_BST.append_node(6)
# obj_BST.append_node(2)
# print(obj_BST.print_BST())




from tkinter.messagebox import RETRY


arr = [2,3,1,2,3]
set_arr = set(arr)
final = []
for i in set_arr:
    if arr.count(i) > 1:
        final.append(i)
print(final)