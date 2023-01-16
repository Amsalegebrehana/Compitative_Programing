# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = dummy = ListNode()
        carry = 0

        while l1 and l2:
            curr_sum = carry + l1.val + l2.val
    
            carry = curr_sum // 10
      
            node.next = ListNode(curr_sum % 10)
            
            l1 = l1.next
            l2 = l2.next
            node = node.next
            
        curr_node = l1 or l2
        while curr_node:
            curr_sum = carry + curr_node.val
            carry = curr_sum // 10
            node.next = ListNode(curr_sum % 10)
            
            curr_node = curr_node.next
            node = node.next
            
        if carry:
            node.next = ListNode(carry)
            
        return dummy.next
            
        