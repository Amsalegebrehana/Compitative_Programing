#leetcode 707. Design Linked List solution

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size=0

    def get(self, index: int) -> int:
        i = 0
        temp = self.head
        if index < 0 or index > self.size:
            return -1
        while temp:
            if i == index:
                return temp.val
            temp=temp.next
            i+=1
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size +=1

    def addAtTail(self, val: int) -> None:
        
        new_node = Node(val)
        # temp = head
        while self.head.next is not None:
            
            self.head = self.head.next
        self.head.next = new_node
        self.size +=1
        
            
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        newnode = Node(val)
        temp = self.head
        i = 0 
        while temp:
            if i == index:
                t = self.head.next.next
                newnode.next = t
                self.head.next = newnode
            self.head = self.head.next
            i+=1
            
        self.size +=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size:
            return -1
        i = 0
        while self.head:
            if i == index:
                self.head.next= self.head.next.next
            self.head = self.head.next
            i+=1
                
        self.size -=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)