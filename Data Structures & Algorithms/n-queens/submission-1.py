class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = set()
        pos_diag = set()
        neg_diag = set()
        board = [["."]*n for i in range(n)]
        result = []
    
        def dfs(r):
            if r == n:
                sub_result = ["".join(row) for row in board]
                result.append(sub_result)
                return
            
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r-c) in neg_diag:
                    continue
                
                board[r][c] = 'Q'
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)

                dfs(r + 1)

                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r- c)
                board[r][c] = '.'
            
        dfs(0)
        return result

