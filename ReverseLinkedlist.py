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
        
        
# def simpleArraySum(ar):
# # Write your code here

#     summ = 0
#     for i in range(0, len(ar)):
#         summ += ar[i]
#     print(summ)

# simpleArraySum([1,2,3])
