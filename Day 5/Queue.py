#-----------------------EVENT DRIVEN PROBLEM(QUEUE)-----------------------#
"""
                             Time Comlexity            Space Complexity
Create Queue                     O(1)                        O(1)
Enqueue                        O(n)/O(1)                     O(1)
Dequeue                        O(n)/O(1)                     O(1)
Peek                             O(1)                        O(1)
isEmpty                          O(1)                        O(1)
Delete Entire Queue              O(1)                        O(1)

"""


import sys
class Queue:
    def __init__(self, size):
        self.myQueue = []
        self.queueSize = size 

    def isFull(self):
        if len(self.myQueue) == size:
            return True 
        else:
            return False

    def enQueue(self, value):
        if self.isFull():
            print("Queue is full")
        else:
            self.myQueue.append(value)

    def display(self, value):  
        print(self.myQueue)

    def isEmpty(self):
        if self.myQueue == []:
            return True 
        else:
            return False  

    def deQueue(self):
        if self.isEmpty():
            return True 
        else:
            self.myQueue.pop(0)   # remove and by indexing not removing first element
        
    def peek(self):
        if self.isEmpty():
            print("Queue is empty") 
        else:
            print(self.myQueue[0])

    def delete(self):
        self.myQueue = None  


size = int(input("Enter the size of the queue : "))
obj = Queue(size)
print("Queue has created")
while True:
    print("1. Enqueue Operation ")
    print("2. Display Queue ")
    print("3. Dequeue Operation ")
    print("4  Peek Operation ")
    print("5. Delete Operation ")
    print("6. Exit")
    choice = int(input("Enter your choice :"))
    if choice == 1:
        value = int(input("Enter the element to add : "))
        obj.enQueue(value)
    elif choice == 2:
        obj.display(value)
    elif choice == 3:
        obj.deQueue() 
    elif choice == 4:
        obj.peek()
    elif choice == 5:
        obj.delete()
    else:
        sys.exit()