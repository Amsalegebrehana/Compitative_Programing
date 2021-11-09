#lipnked lists


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
    # traverse linked list
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            while self.head is not None:
                print(self.head.data) 
                self.head = self.next

s = LinkedList()
s.print_ll()
        
