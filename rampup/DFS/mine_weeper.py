class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        stack = [click]
        while stack:
            x, y = stack.pop()
            n_mines = 0
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (1,1), (-1,1), (1,-1), (-1,-1)]:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == 'M':
                    n_mines += 1
                    
            if n_mines > 0:
                board[x][y] = str(n_mines)
            else:
                board[x][y] = 'B'
            
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (1,1), (-1,1), (1,-1), (-1,-1)]:
                    new_x, new_y = x + dx, y + dy

                    if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == 'E':
                        stack.append((new_x,new_y))
                             
        return board
        