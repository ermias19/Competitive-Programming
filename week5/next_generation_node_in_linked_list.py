# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # dummy=ListNode()
        # head=dummy.next
        stack,answers=[],[]
        counter=-1
        cur=head
        while cur:
            counter+=1
            answers.append(0)
            while stack and stack[-1][1]<cur.val:
                index,val=stack.pop()
                answers[index]=cur.val
            stack.append((counter,cur.val))
            cur=cur.next
        return answers
        
        
        
        
        
        
        