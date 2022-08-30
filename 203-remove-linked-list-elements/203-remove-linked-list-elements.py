# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        temp = dummy
        def rec(temp):
            if not temp:
                return
            if not temp.next:
                return
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
            
            rec(temp)
        rec(temp)
        return dummy.next