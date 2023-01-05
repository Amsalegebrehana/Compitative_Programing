# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 1
        dummy = ListNode(None)
        head2 = dummy

        temp = head
        while temp:
            if i %2 !=0:
                new = ListNode(temp.val)
                head2.next = new
                head2 = head2.next 
            temp = temp.next  
            i +=1
           
        i = 1 
        while head:
            if i %2 ==0:
                new = ListNode(head.val)
                head2.next = new
                head2 = head2.next
              
            head = head.next  
            i +=1

        return dummy.next
        
            