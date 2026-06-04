from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0 
        rows, cols = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r,c):
            queue = deque()
            queue.append((r,c))
            visit.add((r,c))
            
            while(queue):
                r,c = queue.popleft()
                neighbours = [[0,-1],[0,1],[-1,0],[1,0]]

                for dr, dc in neighbours:
                    nr = r + dr
                    nc = c + dc
                    if(0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visit and grid[nr][nc] == "1" ):
                        queue.append((nr,nc))
                        visit.add((nr,nc))

        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == "1" and (i,j) not in visit):
                    dfs(i,j)
                    result += 1

        return result

        