# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        t = head
        i = 0
        while t is not None:
            l+=1
            t= t.next
        mid = (l)//2
        while i < mid:
            if i == mid:
                break
            else:
                head=head.next
            i+=1
        while i < l :
            t = head
            head.next
            i+=1
            return t
            
           