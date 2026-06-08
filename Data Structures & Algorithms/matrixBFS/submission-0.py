class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0,0,0))
        visit.add((0,0))
        result = -1

        while(queue):
            r, c, length = queue.popleft()

            if r == rows - 1 and c == cols - 1:
                result = max(result, length)
                continue
                
            neighbours = [[0,1], [0,-1], [-1,0], [1,0]]

            for dr, dc in neighbours:
                nr = r + dr 
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr,nc) not in visit:
                    queue.append((nr, nc, length + 1))
                    visit.add((nr,nc))
        
        return result
                


        