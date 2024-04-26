"""
import modeule containing singly linked list code 

define a class Stack to implement stack data structure 
by inheriting SLL class
"""

from SLL_for_import import *   #importing all things

class Stack(SLL):
    def __init__(self, start=None):
        super().__init__()      #because like JAVA and C++, python did not automaticaly call it's parent class constructor
        self.item_count=0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count-=1
        else:
            raise IndexError("Underflow")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Empty Stack")
    def size(self):
        return self.item_count
    def print1(self):
        return self.print_list()
    
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print("Top element on the stack: ",s1.peek())
s1.pop()
print("Top element on the stack: ",s1.peek())
print("The total element: ",s1.size())
print("The stack is: ",end=" ")
s1.print1()