#leetcode  Remove Nth data from End of list 

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def add_begning(self, data):
        newdata = Node(data) 
        
        newdata.next = self.head 
        self.head = newdata
    def removeNode(self, n):
        length = 0
        t= self.head
        n = n-1
        while t is not None:
            length +=1
            t=t.next 
        remove_data = self.head 
        num = length - n 
        while length >= 0:
            if length == num:
                remove_data.next = remove_data.next.next 
            else:
                remove_data.next = remove_data.next
            length -= 1
        print("######")
        print("length in remove ", length)
        print("######")
        
    def print_ll(self):
        if self.head is None:
            print("Linked list is empty") 
            
        else:
          while self.head is not None:
              print(self.head.data) 
              self.head = self.head.next
              

nlist = LinkedList() 

nlist.add_begning(5)
nlist.add_begning(4)
nlist.add_begning(3)
nlist.add_begning(1)
nlist.removeNode(1)
nlist.print_ll()