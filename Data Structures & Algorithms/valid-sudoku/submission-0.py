class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0,9):
            hashSet = set()
            for j in range(0,9):
                if(board[i][j] == '.'):
                    continue
                if(board[i][j] in hashSet):
                    return False
                hashSet.add(board[i][j])
              
        for i in range(0,9):
            hashSet = set()
            for j in range(0,9):
                if(board[j][i] == '.'):
                    continue
                if(board[j][i] in hashSet):
                    return False
                hashSet.add(board[j][i])


        for square in range(9):
            hashSet = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3 + i
                    col = (square%3) * 3 + j
                    if(board[row][col] == '.'):
                        continue
                    if(board[row][col] in hashSet):
                        return False
                    hashSet.add(board[row][col])
                
        return True

                    
                    







            
        