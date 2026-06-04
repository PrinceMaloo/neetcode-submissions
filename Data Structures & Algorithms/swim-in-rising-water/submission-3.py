import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        heap = []

        def bfs(row, col):
            heapq.heappush(heap, (grid[row][col],row, col))
            visit.add((row,col))

            while(heap):
                level, r, c = heapq.heappop(heap)
                if r == rows - 1 and c == cols - 1:
                    return level
                
                neighbours = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in neighbours:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visit:
                        next_waterlevel = max(level, grid[nr][nc])
                        heapq.heappush(heap, (next_waterlevel, nr, nc))
                        visit.add((nr,nc))
                
            return grid[row][col]   
        
        return bfs(0,0)
        

        