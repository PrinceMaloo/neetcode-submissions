from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if(grid[0][0] ==1 ):
            return -1
        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        queue = deque()

        visit.add((0,0))
        queue.append((0,0))

        length = 1  

        while(queue):
            for i in range(len(queue)):
                r,c = queue.popleft()
                print("r",r)
                print("c",c)
                neighbours = [[0,-1], [0,1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
                prevSetLength = len(visit)

                if(r == rows-1 and c == cols -1 ):
                    return length 

                for dr,dc in neighbours:
                    nr = r + dr
                    nc = c + dc

                    if(min(nr,nc) < 0 or nr == rows or nc == cols or grid[nr][nc] == 1 
                        or (nr,nc) in visit):
                        continue
                    
                    visit.add((nr,nc))
                    queue.append((nr,nc))

            length += 1
                
                
        
        return -1


        