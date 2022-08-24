class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def solve(i, j):
            if not(0<=i<m and 0<=j<n) or (not grid[i][j]):
                return
            grid[i][j] = 0
            for x, y in dir:
                solve(i+x, j+y)

        for i in range(m):
            for j in range(n):
                if(grid[i][j] and (i*j == 0 or i == m-1 or j == n-1)):
                    solve(i, j)
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += grid[i][j]
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def dfs(i, j):
#             if grid[i][j] == 0:
#                 return
#             grid[i][j] = 0

#             if i: dfs(i - 1, j)
#             if i != m - 1: dfs(i + 1, j)
#             if j: dfs(i, j - 1)
#             if j != n - 1: dfs(i, j + 1)
        
#         for i in range(m):
#             dfs(i, 0)
#             dfs(i, n - 1)
        
#         for j in range(1, n - 1):
#             dfs(0, j)
#             dfs(m - 1, j)
        
#         return sum(num for row in grid for num in row)