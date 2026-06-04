class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        rows,cols = len(grid),len(grid[0])
        pac, atl = set(),set()
        result = []

        def dfs(r,c,visit,prevVal):
            if (r,c) in visit or min(r,c) < 0 or r >= rows or c >= cols or grid[r][c]< prevVal:
                return 
            
            visit.add((r,c))
            dfs(r-1,c,visit,grid[r][c])
            dfs(r+1,c,visit,grid[r][c])
            dfs(r,c-1,visit,grid[r][c])
            dfs(r,c+1,visit,grid[r][c])

        for i in range(cols):
            dfs(0,i,pac,grid[0][i])
            dfs(rows  - 1,i,atl,grid[rows - 1][i])

        for i in range(rows):
            dfs(i,0,pac,grid[i][0])
            dfs(i,cols-1,atl,grid[i][cols - 1])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
                
        return result