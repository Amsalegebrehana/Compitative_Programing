"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        curr = head
        
        while curr:
            if curr.child:
              
                next_node = curr.next

                child_head = self.flatten(curr.child)
                curr.next = child_head
                child_head.prev = curr

                child_tail = child_head
                while child_tail.next:
                    child_tail = child_tail.next
                child_tail.next = next_node
                if next_node:
                    next_node.prev = child_tail
                curr.child = None
                curr = child_tail
            else:
                curr = curr.next

        return head







