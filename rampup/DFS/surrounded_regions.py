class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n=len(board), len(board[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        border= lambda row,column: 0<=row<m and 0<=column<n
        def surr_regions(r,c):
            if border(r, c) and board[r][c] == 'O':
                board[r][c] = 'M'
                for x, y in directions:
                    surr_regions(r+x, c+y)
                    
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    surr_regions(i,j)
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                    
      
        