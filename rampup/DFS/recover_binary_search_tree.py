# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(root):
            
            if not root:
                return
            inorder(root.left)
            if self.prev and root.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.last = root
            self.prev = root
            inorder(root.right)
        
        self.first = self.last = self.prev = None
        inorder(root)
        self.first.val, self.last.val = self.last.val, self.first.val