# import modeule containing singly 
# linked list code in your python file and do

from SLL_for_import import *   #importing all things

class Stack:
    def __init__(self):
        self.myList=SLL()
        self.item_count=0
    def is_empty(self):
        return self.myList.is_empty()
    def push(self,data):
        self.myList.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.myList.delete_first()
            self.item_count-=1
    def peek(self):
        if not self.is_empty():
            return self.myList.start.item
    def size(self):
        return self.item_count
    def print1(self):
        self.myList.print_list()


s=Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top element is: ",s.peek())
s.pop()
s.print1()