def has_cycle(head):
    slow=fast=head
   

    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            return True
    
    return False
        