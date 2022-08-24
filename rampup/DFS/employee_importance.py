"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {}
        imp = {}
        
        for i in range(len(employees)):
            graph[employees[i].id] = employees[i].subordinates
            imp[employees[i].id] = employees[i].importance
        
        vis = set()
        res = [0]
        def dfs(i):
            if i in vis:
                return
            
            vis.add(i)
            res[0] += imp[i]
            for k in graph[i]:
                dfs(k)
                
        dfs(id)
        
        return res[0]