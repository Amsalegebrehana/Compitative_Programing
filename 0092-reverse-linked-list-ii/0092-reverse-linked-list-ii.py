# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(currHead, left, right):
            prev = None
            temp = tail = currHead
            while temp and left < right + 1:
                curr = temp.next
                temp.next = prev
                prev = temp
                temp = curr
                left += 1
            return prev, tail
        leftHead , rightHead = ListNode(None, head), ListNode(None, head)
        templ = leftHead
        tempr = rightHead
        prev = None
        cl = cr = 0
        while cl < left:
            prev = templ
            templ = templ.next
            cl += 1
        while cr < right+1:
            tempr = tempr.next
            cr+=1

        revhead, revtail = reverse(templ, left, right)
     
        prev.next = revhead
  
        while prev.next:
            prev = prev.next
      
        prev.next = tempr
     
        return leftHead.next
        
            
                