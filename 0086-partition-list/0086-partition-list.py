# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        left = ListNode(0)
        right = ListNode(0)
        l = left
        r = right
        
        while head:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                r.next = head
                r = r.next
                
            head = head.next
            
        l.next = right.next
        r.next = None
        
        return left.next