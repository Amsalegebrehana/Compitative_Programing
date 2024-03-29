#hacker rank Cycle Detection solution

#slow fast pointers approach

def has_cycle(head):
    slow = head
    fast = head
    while fast and slow and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return 1
        
    return 0