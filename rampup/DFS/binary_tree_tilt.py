class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res=0
        self.result=0
        def tilt(r):
            
            if not r:
                return 0
            left, right = tilt(r.left), tilt(r.right)
            
            # nonlocal   res
            # self.result+=abs(left-right)
            self.res+=r.val+left+right
            # res+=r.val +left+right
            return r.val+left+right
            
        tilt(root)
        return self.res
        

    
#         def helper(root):
#             if root is None:
#                 return 0
            
#             left, right = helper(root.left), helper(root.right)
#             self.res += abs(left - right)
#             return root.val + left + right
        
#         helper(root)
#         return self.res
