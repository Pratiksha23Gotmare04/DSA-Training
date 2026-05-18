#------------------------- LINKED LIST -------------------------#

# class Node:
#     def __init__(self, data):
#         self.data = data             # instance variable
#         self.next = None 

# class LinkedList:
#     def __init__(self):
#         self.head = None 

# linkedlist = LinkedList()
# linkedlist.head = Node(5)
# second          = Node(10)
# third           = Node(15)
# fourth          = Node(20)

# # connecting a node
# linkedlist.head = second
# second.next = third 
# third.next = fourth

# # display linked list
# while linkedlist.head != None:
#     print(linkedlist.head.data, "|", linkedlist.head.next,"->", end = " ")
#     linkedlist.head = linkedlist.head.next

#---------------------------- DYNAMIC WAY -------------------------------#
# Why execution start from main() only = 

import sys
class Node:
    def __init__(self, data):
        self.data = data           # instance variable
        self.next = None  

class Linledlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, value):
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node 
        else:
            self.tail.next = self.node
            self.tail = self.node 

    def addNodeBegining(self, value):
        print("Add Node Begining")
        self.node = Node(value)
        if self.head is None:
            self.head = self.node 
            self.tail = self.node 
        else:
            self.node.next = self.head
            self.head = self.node

    def display(self, value):
        while self.head is not None:
            print(self.head.data, '|', '->', end = ' ')
            self.head = self.head.next
        print()


if __name__ == '__main__':
    obj = Linledlist()
    while True:
        print("1. Add Node into LinkedList  ")
        print("2. Add Node in Begining  ")
        print("3. Add Node in Between  ")
        print("4. Add Node in End  ")
        print("5. Display LinkedList  ")
        print("6. Exit : ")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            value = int(input("Enter value of a node : "))
            obj.addNode(value)
            print("Node added successfully in Single LinkedList")

        elif choice == 2:
            value = int(input("Enter value of a node : "))
            obj.addNodeBegining(value)
            print("Node added successfully at the Begining of LinkedList")

        elif choice == 5:
            obj.display(value)
        else:
            sys.exit()
