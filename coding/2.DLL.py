""" Doubly Linked List """

class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():    #when previously node present
            self.start.prev=n
        self.start=n
    def insert_at_end(self,data):
        temp=self.start
        if self.start != None:
            while temp.next != None:    
                temp=temp.next

        n=Node(temp,data,None)
        if temp==None:    #when no previous element present
            self.start=n
        else:
            temp.next=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.data==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:     # when is not last node
                temp.next.prev=n
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.data,end=' ')
            temp=temp.next
    def delete_first(self):
        if self.start is not None:    
            self.start=self.start.next
            if self.start is not None:    #when 2nd node present
                self.start.prev=None
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:   #when one node only 
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
    def delete_item(self,data):
        if self.start is None:   #empty when
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.data==data:
                    if temp.next is not None:    #when right node is present
                        temp.next.prev=temp.prev
                    if temp.prev is not None:    #when left node is present
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next  #when only one node
                    break
                temp=temp.next
    def __iter__(self):
        return DLLIterator(self.start)
class DLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current=self.current.next
        return data
    

myList=DLL()
myList.insert_at_start(10)
myList.insert_at_end(20)
myList.insert_after(myList.search(10),15)
for x in myList:
    print(x,end=' ')



            
