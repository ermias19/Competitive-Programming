class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        slow=head
        fast=head
        while fast and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
        