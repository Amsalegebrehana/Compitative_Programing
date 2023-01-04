# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reversl(head):
            prev = None
            curr = head
            while curr:
                new = curr.next
                curr.next = prev
                prev = curr
                curr = new
            return prev
        temp = reversl(head)
        

        curr = temp.next
        st=[temp.val]
       
        while curr:
            if st and st[-1] <= curr.val:
     
            
                st.append(curr.val)
            curr = curr.next
        dummy = ListNode(None) 
        t = prev = dummy
       
        st = st[::-1]

        for i in st:
     
            newnode = ListNode(i)
            newnode.next = prev
            prev =newnode
        
        h = reversl(prev)

        return h.next
        
            

        
            