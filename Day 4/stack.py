#---------------------------- STACK ----------------------------#
"""
stack implementation without size limit
 stack implementation with size limit 
There are two ways
1. List/Array
2. Linkedlist

Use of Class = 
Can be reused, can create as many method
Class first character always capital
Use of Object = 
Role of data member = means variable

Stack using List
- Easy to implement 
- Speed problem when it grows 

Stack using Linked List
- Fast performance
- Implementation is not easy

                             Time Comlexity            Space Complexity
Create Stack                     O(1)                        O(1)
Push                           O(1)/O(n^2)                   O(1)
Pop                              O(1)                        O(1)
Peek                             O(1)                        O(1)
isEmpty                          O(1)                        O(1)
Delete Entire Stack              O(1)                        O(1)

"""

# class Name:
#     def __init__(self):    # self = default argument
#         self.name = "Pratiksha"
#         self.age = 22

#     def display(self):
#         print("Name : ", self.name)
#         print("Age : ", self.age)

# stuObj = Name()
# stuObj.display()
# print(stuObj)
# print(stuObj.name)
# print(stuObj.age)

#---------------------------- DEFAULT CONSTRUCTOR ----------------------------#
# class Message:
#     def __init__(self):
#         print("I am constructor")

#     def shows(self):
#         print("Class program")
    
# obj = Message()
# obj.shows()
# obj1 = Message()

#---------------------------- PARAMETERIZED CONSTRUCTOR ----------------------------#
# class StudentInfo:
#     def __init__(self, name, age, roll_no):
#         self.Name = name 
#         self.Age = age 
#         self.RollNo = roll_no 

#     def displayStudentInfo(self):
#         print("Name = ", self.Name)
#         print("Age = ", self.Age)

# stuObj = StudentInfo("Pratiksha", 22, 44)
# stuObj.displayStudentInfo()

#--------------------------------- STACK -----------------------------------#
# menu - driven program
# peek operation = just return the top most element
# pop operation = removes the topmost element permanently

# import sys
# class Stack:
#     def __init__(self):
#         self.myStack = []

#     def push(self, value):
#         self.myStack.append(value)
#         print("Element Push")

#     def display(self):
#         print(self.myStack) 

#     def isEmpty(self):
#         if self.myStack == []:
#             return True 
#         else:
#             return False 
        
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print(self.myStack.pop())

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print(self.myStack[-1])

#     def delete(self):
#         self.myStack = None


# obj = Stack()
# print("Stack has created : ")
# while True:
#     print("1. Push Operation")
#     print("2. Diaplsy Stack")
#     print("3. Pop Operation")
#     print("4. Peek Operation")
#     print("5.Delete Operation")
#     print("7. Exit ")
  
#     choice = int (input("Enter your choice : "))
#     if choice == 1:
#         value = int(input("Enter value to push in stack : "))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.pop()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.delete()
#     else:
#         sys.exit()

#------------------------ WITH SIZE LIMIT -----------------------------------#
# Now we have to implement stack with size limit 
import sys
class Stack:
    def __init__(self, size):
        self.myStack = []
        self.stackSize = size 

    def isFull(self):
        if len(self.myStack) == self.stackSize:
            return True 
        else:
            return False

    def push(self, value):
        if self.isFull():
            print("Stack is full")
        else:
            self.myStack.append(value)
            print("Element Push")

    def display(self):
        print(self.myStack) 

    def isEmpty(self):
        if self.myStack == []:
            return True 
        else:
            return False 
        
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.myStack.pop())

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.myStack[-1])

    def delete(self):
        self.myStack = None

size = int(input("Enter the size of the stack : "))
obj = Stack(size)
print("Stack has created : ")
while True:
    print("1. Push Operation")
    print("2. Diaplay Stack")
    print("3. Pop Operation")
    print("4. Peek Operation")
    print("5. Delete Operation")
    print("7. Exit ")
  
    choice = int (input("Enter your choice : "))
    if choice == 1:
        value = int(input("Enter value to push in stack : "))
        obj.push(value)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.pop()
    elif choice == 4:
        obj.peek()
    elif choice == 5:
        obj.delete()
    else:
        sys.exit()

#--------------------------------------------------------#

"""
Student Management System
1. Add Student
2. Show Student
3. Update Student
4. Delete Student
5. Exit

Select any choice : 1
Enter student id, rollno , name, city

Select any choice : 2
Id : 1      
Roll No : 44
Name : Pratiksha
City : Pune

Select any choice : 3
Enter student id :
Match student data are:

Select any choice : 4
Enter student id :
Do you really want to delete this student data (Y/N) : Y
"""