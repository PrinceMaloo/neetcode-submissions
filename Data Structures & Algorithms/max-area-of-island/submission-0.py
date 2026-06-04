class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        visit= set()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            area = 0
            queue= deque()
            visit.add((r,c))
            queue.append((r,c))

            while(queue):
                r,c = queue.popleft()
                neighbours = [[0,-1],[0,1],[-1,0],[1,0]]
                area += 1
                for dr,dc in neighbours:
                    nr = r + dr
                    nc= c + dc
                    if(0<=nr < rows and 0<=nc < cols and (nr,nc) not in visit and grid[nr][nc] == 1):
                        queue.append((nr,nc))
                        visit.add((nr,nc))
            
            return area
                
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 1 and (i,j) not in visit):
                    result = max(result, bfs(i,j))
                
        return result


        