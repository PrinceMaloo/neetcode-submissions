class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        rows,cols = len(grid),len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False]*cols for _ in range(rows)]
        atl = [[False]*cols for _ in range(rows)]
        result = []

        def bfs(array,ocean):
            queue = deque(array)
            while(queue):
                r,c = queue.popleft()
                ocean[r][c] = True
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if(0 <= nr < rows and 0 <= nc < cols and not ocean[nr][nc] and grid[nr][nc] >= grid[r][c]):
                        queue.append((nr,nc))
            
            return 
                
            

        atlantic = []
        pacific = []
        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows- 1 ,c))
        
        for r in range(rows):
            pacific.append((r,0))
            atlantic.append((r,cols-1))

        bfs(pacific,pac)
        bfs(atlantic,atl)
        
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    result.append([r,c])
                
        return result