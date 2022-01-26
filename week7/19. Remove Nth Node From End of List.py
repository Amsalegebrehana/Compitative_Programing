# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length +=1
        print(length)
        temp2 = head
        idx=0
        if head.next is None:
            head = head.next
        while temp2:
            if idx == (length - n)-1:
                temp2.next = temp2.next.next
                break
            temp2=temp2.next
            idx +=1
        return head
        