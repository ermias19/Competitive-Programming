# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def LCN(r,level):
            nonlocal ans, deepest_level
            deepest_level=max(deepest_level,level)
            if not r:
                return level 
            left=LCN(r.left,level+1)
            right=LCN(r.right,level+1)
            
            if left ==right==deepest_level:
                ans=r
            return max(left,right)
        deepest_level=0
        ans=None
        LCN(root,0)
        return ans
            
        
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
#         return self.helper(root,0)[0]
        
#     def helper(self, root, height):
#         if root is None:
#             return (None,0)
#         left=self.helper(root.left, height)
#         right=self.helper(root.right,height)
        
#         if left[1]==right[1]:
#             return (root,left[1]+1)

#         if left[1]>right[1]:
#             return (left[0],left[1]+1)
        
#         if left[1]<right[1]:
#             return (right[0],right[1]+1)
        