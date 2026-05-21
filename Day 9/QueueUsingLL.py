#---------------------- QUEUE USING LINKED LIST ----------------------#

class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next 

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    def enQueue(self, value):
        newNode = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = newNode 
            self.LinkedList.tail = newNode 
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode 

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
        
    def deQueue(self):
        if self.isEmpty():
            return " There is no element in the Queue"
        else:
            tempnode = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
            return tempnode

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.LinkedList.head 
        
    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None 

customQueue = Queue()
customQueue.enQueue(1)
customQueue.enQueue(2)
customQueue.enQueue(3)
print(customQueue)
print("Display Top value")
print(customQueue.peek())
print("Delete FIFO Element")
print(customQueue.deQueue())
print("Now check the queue again")
print(customQueue)
print("Delete FIFO Element")
print(customQueue.deQueue())
print("Now check the queue again")
print(customQueue)
                
            
