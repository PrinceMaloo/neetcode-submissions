class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])


        def capture(r,c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O'):
                return
            
            board[r][c] = 'T'
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

        for i in range(cols):
            if(board[0][i] == 'O'):
                capture(0,i)
            if(board[rows-1][i] == 'O'):
                capture(rows-1,i)
        
        for i in range(rows):
            if(board[i][0] == 'O'):
                capture(i,0)
            if(board[i][cols-1] == 'O'):
                capture(i,cols - 1)
            
        for i in range(rows):
            for j in range(cols):
                if(board[i][j] == 'T'):
                    board[i][j] = 'O'
                elif(board[i][j] == 'O'):
                    board[i][j] = 'X'
                else:
                    continue