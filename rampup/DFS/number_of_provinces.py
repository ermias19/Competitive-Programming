class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.find_row, self.find_column=len(isConnected)-1,len(isConnected[0])-1
        self.counter=0
        def num_prov(r, j):
            
            for row in range(len(isConnected)):
                for column in range(len(isConnected[row])):
                    if isConnected[r][r]:
                            self.counter=1
                    if isConnected[r][j]==1:
                        self.counter+=1
                    # else:
                    #     self.counter+=1
                    if r<self.find_row:Num_prov(r+1,j)
                    if j<self.find_column:Num_prov(r,j+1)
        num_prov(self.find_row,self.find_column)
        return self.counter
    
          
    

        
                
        
                
            
            
            
        
        
        
        
   

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         graph = defaultdict(list)
#         for i,x in enumerate(isConnected):
#             for j,n in enumerate(x):
#                 if j!=i and n == 1:
#                     graph[i].append(j)
            
#         visit = set()
        
#         def dfs(node):
#             if node not in graph:
#                 return 
#             for neighbor in graph[node]:
#                 if neighbor not in visit:
#                     visit.add(neighbor)
#                     dfs(neighbor)
#         count = 0
#         for i in range(len(isConnected)):
#             if i in visit:
#                 continue
#             count+=1
#             dfs(i)
#         return count