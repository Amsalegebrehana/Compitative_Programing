# #linked list

# class Node:
#     def __init__(self, data,next=None):
#         self.data = data 
#         self.next = next 
        
# class LinkedList:
#     def __init__(self):
#         self.head = None 
#     # addinng
#     def add_begning(self,data):
#        new_node = Node(data)
#        new_node.next = self.head 
#        self.head = new_node
        
#     # traversal 
#     def print_ll(self):
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             while self.head is not None:
#                 print(self.head.data)
#                 self.head = self.head.next
            
# # lists = LinkedList()
# # lists.add_begning(4)
# # lists.add_begning(5)
# # lists.print_ll()

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
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
        else:
            length = 0
            t= self.head
            while t is not None:
                length +=1
                t=t.next
            # if lenght 
            mid = length // 2
            count = 0
            mid_data = self.head 
            while count < mid:
                mid_data = mid_data.next 
                count += 1 
            new_data.next = mid_data.next
            mid_data.next = new_data 
            
            print("mid_data", mid_data.data) 
            print("mid", mid) 
            print("lenght is ",length)
    def add_end(self, data):
        newdata= Node(data)
        if self.head is None:
            self.head = newdata 
        else:
            temp = self.head 
            while temp.next is not None:
                temp = temp.next 
            temp.next = newdata
    def removeNode(self, n):
        length = 0
        t= self.head
        n = 0
        while t is not None:
            length +=1
            t=t.next 
        remove_data = self.head 
        num = length - n 
        while length > 0:
            if length == num:
                remove_data.next = remove_data.next.next 
            else:
                remove_data = remove_data.next
        print("######")
        print("length in remove ", length)
        print("######")
        
    def delete_at_end(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            t =self.head 
            while t.next.next is not None:
                t = t.next
                
            t.next = None
            
            print("end data", t.data)
    def delete_begining(self):
         if self.head is None:
            print("Linked list is empty")
         else:
            self.head = self.head.next 
   
            
    def print_ll(self):
        count = 0
        if self.head is None:
            print('linked list is empty')
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.next

l = LinkedList() 
l.add_begining(1)
l.add_begining(2)
l.add_begining(3)
l.add_end(4)
l.add_end(5)
l.add_begining(6)
l.add_middle(3)
l.removeNode(0)

# l.delete_at_end()
# l.delete_begining()


l.print_ll()
# print(len(l))
    