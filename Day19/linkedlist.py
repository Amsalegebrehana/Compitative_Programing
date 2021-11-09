#linked list

class Node:
    def __init__(self, data,next=None):
        self.data = data 
        self.next = next 
        
class LinkedList:
    def __init__(self):
        self.head = None 
    # addinng
    def add_begning(self,data):
       new_node = Node(data)
       new_node.next = self.head 
       self.head = new_node
        
    # traversal 
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.next
            
# lists = LinkedList()
# lists.add_begning(4)
# lists.add_begning(5)
# lists.print_ll()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
    def add_begining(self, data):
        new_data = Node(data) 
        new_data.next = self.head 
        self.head = new_data
    def add_middle(self, data):
         pass
    def add_end(self, data):
        newdata= Node(data)
        if self.head is None:
            self.head = newdata 
        else:
            temp = self.head 
            while temp.next is not None:
                temp = temp.next 
            temp.next = newdata
    def print_ll(self):
        if self.head is None:
            print('linked list is empty')
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.next

l = LinkedList() 
l.add_begining(5)
l.add_begining(5)
l.add_begining(5)
l.add_end(3)
l.add_end(4)
l.add_begining(2)

l.print_ll()
    