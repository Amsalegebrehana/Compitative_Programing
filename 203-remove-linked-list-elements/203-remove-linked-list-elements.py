# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(seelf, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        temp = dummy
        def rec(temp):
            if temp and temp.next:
                if temp.next.val == val:
                    temp.next = temp.next.next
                    rec(temp)
                else:
                    rec(temp.next)
         
        rec(temp)
        return dummy.next
        