#leetcode reverse linked list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = head
        prev =None 
        while val is not None:
             next = val.next
             val.next = prev
             prev = val
             val = next 
        return prev
        
        

