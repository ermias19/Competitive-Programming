
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
       
           
            
            print(slow.val,fast.val)
        return slow
            
           
        
        
        
        
        
        
        
        
        
        
        
        