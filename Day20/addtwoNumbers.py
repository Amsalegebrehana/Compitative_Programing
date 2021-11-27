#leetcode 2 Add two Numbers Solution 

def add_nums(l1,l2):
    node = ListNode()
    current_node = node
    head = None 
    temp = None
    while l1 or l2:
        data1 = l1.val if l1 else 0 
        data2 = l2.val if l2 else 0
        carry = 0 
        
        # new digit
        val = data1 + data2 + carry 
        carry = 1 if val > 9 else 0
        val = val%10
        current_node.next = ListNode(val)
        current_node = current_node.next 
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None 
    return node.next
        