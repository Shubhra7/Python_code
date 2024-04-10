class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class CLL:
    def __init__(self,last=None):
        self.last=last

    def is_empty(self):
        return self.last == None
    
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n

    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n

    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp != self.last:  #upto 2nd last node check done
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item == data:
            return temp
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp == self.last:   # if temp is last node then have to update the last
                self.last=n

    def print_list(self):
        if not self.is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item,end=' ')
                temp=temp.next
            print(temp.item)
    
    def delete_first(self):
        if not self.is_empty():
            temp=self.last
            if temp.next==self.last:   #when single node present
                self.last=None
            else:
                self.last.next=temp.next

    def delete_last(self):
        if not self.is_empty():
            temp=self.last
            if temp.next==self.last:    #when single node present
                self.last=None
            else:
                temp=temp.next
                while temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp
        
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next==self.last:    
                if self.last.item==data:     # if only node and mathced with the data
                    self.last=None
            else:
                if self.last.next.item==data:   # multiple node and mathced with first node
                    self.delete_first()
                else:
                    temp=self.last.next
                    while temp!=self.last:
                        if temp.next == self.last:
                            if self.last.item == data:   # multiple node and mathced with last node 
                                self.delete_last()
                            break
                        if temp.next.item == data:         # multiple node and mathced with any middle node 
                            temp.next=temp.next.next
                            break
                        temp=temp.next
    def __iter__(self):
        if self.last==None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)   #sending first node address

class CLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current == None:
            raise StopIteration
        
        if self.current== self.start and self.count==1:   #for stop the iteration like temp!=self.last
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next

        return data
    

cll=CLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_after(cll.search(10),50)
for x in cll:
    print(x,end=' ')
print()
cll.print_list()
                    




 






    