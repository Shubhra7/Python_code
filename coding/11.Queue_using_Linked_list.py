"""
Define a class Queue to implement queue data structure using singly
linked list concept.
Define __init__() method to initialise front and rear reference variable;
and item_count variable to keep track of number of elements in the queue

"""
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
    
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.front==None
        # return self.rear==None
        # return self.item_count==0
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
            self.rear=n
        else:
            self.rear.next=n
            self.rear=n
        self.item_count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty(Underflow)")
        elif self.front == self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.item_count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("No data in the queue")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("No data in the queue")
        else:
            return self.rear.item
    def size(self):
        return self.item_count
    def print_queue(self):
        temp=self.front
        print("The queue is: ",end=" ")
        print("|",end="")
        while temp is not None:
            print(temp.item,"|",end=" ")
            temp=temp.next
    


q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("Front item is: ",q1.get_front(),"\nRear item is: ",q1.get_rear())
q1.dequeue()
print()
print("Front item is: ",q1.get_front(),"\nRear item is: ",q1.get_rear())
q1.print_queue()
