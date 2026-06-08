class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        
        def dfs(i,j):
            if min(i,j) < 0 or i == rows or j == cols or (i,j) in visit or grid[i][j] == 1:
                return 0
            
            if i == rows - 1 and j == cols - 1:
                return 1
            
            visit.add((i,j))
            neighbours = [[0,1], [0,-1], [-1,0], [1,0]]
            result = 0

            for dr, dc in neighbours:
                r = i + dr
                c = j + dc
                result += dfs(r,c)
            
            visit.remove((i,j))        

            return result
        
        return dfs(0,0)
            


        