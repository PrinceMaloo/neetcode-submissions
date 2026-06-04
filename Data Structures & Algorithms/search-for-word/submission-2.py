class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        characterIncluded = {}
        for i in range(rows):
            for j in range(cols):
                if(self.WordExist(board, word,i,j, "",characterIncluded)):
                    return True
            
        return False
    
    def WordExist(self,board,word,i,j,currentWord,characterIncluded):
        currentWord += board[i][j]
        characterIncluded[(i,j)] = True
        
        if(len(currentWord) == len(word)):
            characterIncluded[(i,j)] = False
            if(currentWord == word):
                return True
            return False

        if(i + 1 < len(board) and not characterIncluded.get((i+1,j),False)):
            if(self.WordExist(board,word,i+1,j,currentWord,characterIncluded)):
                return True
        
        if(i - 1 >= 0 and not characterIncluded.get((i-1,j),False)):
            if(self.WordExist(board,word,i-1,j,currentWord,characterIncluded)):
                return True

        if(j+1 < len(board[0])  and not characterIncluded.get((i,j+1),False)):
            if(self.WordExist(board,word,i,j+1,currentWord,characterIncluded)):
                return True
        
        if(j-1 >= 0  and not characterIncluded.get((i,j-1),False)):
            if(self.WordExist(board,word,i,j-1,currentWord,characterIncluded)):
                return True
        
        characterIncluded[(i,j)] = False
        return False
        