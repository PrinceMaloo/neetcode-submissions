class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        result = 0
        for r in range(rows):
            for c in range(cols):
                neighbours = [[0,1],[0,-1],[1,0],[-1,0]]
                if(grid[r][c] != 1):
                    continue
                count = 4
                print("r",r)
                print("c",c)
                for dr,dc in neighbours:
                    nr = r + dr
                    nc = c + dc
                    print("nr1",nr)
                    print("nc1",nc)
                    if(min(nr,nc) >= 0 and nr< rows and nc < cols and grid[nr][nc] == 1):
                        print("nr",nr)
                        print("nc",nc)
                        count -= 1
                result += count

        
        return result

        