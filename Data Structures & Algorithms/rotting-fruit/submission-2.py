class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        queue = deque()
        length = -1

        def AddCell(r,c):
            if(0 <=r < rows and 0 <= c < cols and (r,c) not in visit and 
                grid[r][c] == 1):
                grid[r][c] = 2
                queue.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 2):
                    queue.append((r,c))

        while(queue):
            for i in range(len(queue)):
                r,c = queue.popleft()
                if grid[r][c] == 2 and (r,c) not in visit:
                    AddCell(r+1,c)
                    AddCell(r-1,c)
                    AddCell(r,c-1)
                    AddCell(r,c+1)
                    visit.add((r,c))  

            length += 1
        
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == 1):
                    return -1

        return 0 if length == -1 else length

        