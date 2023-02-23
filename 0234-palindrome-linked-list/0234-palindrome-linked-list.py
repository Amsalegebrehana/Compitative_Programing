# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        reverse = None 
        while temp is not None:
            node = ListNode(temp.val)
            node.next= reverse
            reverse = node
            temp = temp.next
        while head and reverse:
            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next
        return  True
        