# single linked list
#not need to think about memory management because 
#in python gurbage collection done automatically

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:   # head pointer
    def __init__(self, start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():   #checking ll is empty?
            temp=self.start
            while temp.next is not None:  #traversing
                temp=temp.next
            temp.next=n
        else:
            self.start=n   #if empty then=> start contatin new node
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp.next is not None:
            print(f'|{temp.item}|',end=' ')
            temp=temp.next
        print(f'|{temp.item}|')
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_last(self):
        if self.start is None:    # if list is empty
            pass  
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:  #going 2nd last node
                temp=temp.next
            temp.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None and self.start.item==data:   #if only node and match with the data
            self.start=None
        else:
            temp=self.start
            if temp.item==data:   # if the first item have to delete
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):       # for making the LL iterable
        return SLLIterator(self.start)
class SLLIterator:   # explicitly making the LL iterable***
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:    
            raise StopIteration    # making stop iteration by creating exceptions
        data=self.current.item
        self.current=self.current.next
        return data
            

# driver code
myList=SLL()
myList.insert_at_start(20)
myList.insert_at_start(30)
myList.insert_at_start(40)
myList.insert_at_start(50)
myList.insert_after(myList.search(30),99)
myList.print_list()
myList.delete_item(30)
print()
myList.print_list()
print('\nPrinting by making the Object iterable: ')
for x in myList:    # first need to make our object iterable
    print(x,end=' ')
print()
