"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
     
        self.result=[]
        self.path=0
        if not root:
            return 0
        def depth(r,result,path):
            if not r.children:
                self.result.append(path)
                return 0
            for i in range(len(r.children)):
                depth(r.children[i],result,path+1)
            print(self.result)

        depth(root,self.result,self.path)
        return max(self.result)+1
        
        
        
        
        
        
        # if not root:
        #     return 0
        # if not root.children:
        #     return 1
        # cur_max=1
        # for i in range(len(root.children)):
        #     depth=self.maxDepth(root.children[i])
        #     cur_max=max(cur_max, 1+depth) 
        # return cur_max 
            


        
        
        
        
        
        

    
    
    
    
    
    
    




         












            