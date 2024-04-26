""" Circular Double Linked List """

class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next

class CDLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        self.start=n

    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n

    def search(self,data):
        temp=self.start
        if temp == None:
            return None
        if temp.item==data:
            return temp
        else:
            temp=temp.next
            while temp != self.start:
                if temp.item==data:
                    return temp
                temp=temp.next
            return None
        
    def insert_after(self,temp,data):   #temp is coming after searching
        if temp != None:
            n=Node(data)
            n.next=temp.next
            n.prev=temp
            temp.next.prev=n
            temp.next=n

    def print_list(self):
        temp=self.start
        if temp is not None:
            print(temp.item,end=' ')   #printing the first element
            temp=temp.next
        while temp is not self.start:    #condition to print
            print(temp.item,end=' ')
            temp=temp.next

    def delete_first(self):
        temp=self.start
        if temp is not None:
            if temp.next==temp:
                self.start=None
            else:
                temp.next.prev=temp.prev
                temp.prev.next=temp.next
                self.start=temp.next

    def delete_last(self):
        temp=self.start
        if temp is not None:
            if temp.next==temp:
                self.start=None
            else:
                temp.prev.prev.next=self.start
                temp.prev=temp.prev.prev
        
    def delete_item(self,data):
        if self.start is not None:
            if self.start.item == data:
                self.delete_first()
            elif self.start.prev.item == data:
                self.delete_last()
            else:
                temp=self.start.next
                while temp != self.start:
                    if temp.item == data:
                        temp.prev.next=temp.next
                        temp.next.prev=temp.prev
                    temp=temp.next
    def __iter__(self):
        return CDLLIterator(self.start)

class CDLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data
    

myList= CDLL()
myList.insert_at_start(10)
myList.insert_at_last(20)
myList.insert_at_last(30)
myList.insert_at_last(40)
myList.print_list()
print()
myList.insert_after(myList.search(30),35)


for x in myList:
    print(x,end=' ')

print()
                




        