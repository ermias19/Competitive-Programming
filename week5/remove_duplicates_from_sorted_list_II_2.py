class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node, previous):
            if not node:
                return
            child = 101
            if node.next:
                child = node.next.val
				# if we didn't use fake head and fake child 
				# the condition of checking is pretty complicated!
            if previous != node.val and node.val != child:
                node.next = helper(node.next, node.val)
                return node
            else:
                return helper(node.next, node.val)
        return helper(head, -101)