class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        queue = deque()
        length = 0
        fresh = 0

        def AddCell(r,c):
            if(0 <= r < rows and 0 <= c < cols and (r,c) not in visit and 
                grid[r][c] == 1):
                nonlocal fresh
                grid[r][c] = 2
                queue.append((r,c))
                fresh = fresh - 1

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 2):
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        while(fresh > 0 and queue):
            for i in range(len(queue)):
                r,c = queue.popleft()
                if grid[r][c] == 2 and (r,c) not in visit:
                    AddCell(r+1,c)
                    AddCell(r-1,c)
                    AddCell(r,c-1)
                    AddCell(r,c+1)
                    visit.add((r,c))  

            length += 1
        
        return length if fresh == 0 else -1

        