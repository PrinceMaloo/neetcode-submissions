class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(i, j, curr):
            if word == curr:
                return True
            
            if min(i, j) < 0 or i >= rows or j >= cols or (i, j) in visit or len(curr) >= len(word):
                return False
            
            ch = board[i][j]
            visit.add((i, j))
            neighbours = [[0,1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in neighbours:
                r = i + dr
                c = j + dc
                if dfs(r, c, curr + ch):
                    return True
            
            visit.remove((i, j))        
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visit = set()
                    if dfs(i, j, ""):
                        return True
            
        return False
            