"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        
        oldnew = {}
        
        while temp:
            
            newNode = Node(temp.val)
            oldnew[temp] = newNode
            temp = temp.next
      
        temp = head
     
        while temp:
            curr = oldnew[temp]
            curr.next = oldnew.get(temp.next, None)
            curr.random = oldnew.get(temp.random, None)
            temp = temp.next
        
       
        return oldnew.get(head, None)