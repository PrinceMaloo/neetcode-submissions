class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cnt = 0
        def dfs(r, c):
            if min(r,c ) < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            neighbours = [[0, 1], [-1, 0], [0, -1], [1, 0]]
            for dr, dc in neighbours:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    cnt += 1
        
        return cnt
        




        
        