# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.result=[]
        def path_sum(r,path):
            if not r:
                return 0
            if not r.left and not r.right:
                path+=[r.val]
                self.result.append(path)

            path_sum(r.left,path+[r.val])
   
            path_sum(r.right,path+[r.val])
        path_sum(root,[])
        for arr in self.result:
            sum_arr=sum(arr)
            if sum_arr==targetSum:
                return True
        return False
                