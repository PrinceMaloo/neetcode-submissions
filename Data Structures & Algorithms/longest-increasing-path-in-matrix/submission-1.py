class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        result = 0
        dp = {}

        def dfs(r, c, visit):
            if min(r,c) < 0 or r == rows or c == cols:
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            
            visit.add((r,c))
            
            neighbours = [[0,1], [1, 0], [0, -1], [-1,0]]
            result = 1
            for (dr, dc) in neighbours:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visit and matrix[nr][nc] > matrix[r][c]:
                    result = max(result,1 + dfs(nr, nc, visit))

            visit.remove((r,c))
            dp[(r,c)] = result
            
            return dp[(r,c)]
        
        for i in range(rows):
            for j in range(cols):
                result = max(result, dfs(i,j, set()))
               
        return result
        

