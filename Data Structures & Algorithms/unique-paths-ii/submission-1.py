class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        cache = {}

        def bfs(r,c,cache):
            if(r >= rows or c >= cols or obstacleGrid[r][c] == 1):
                return 0
            
            if(r == rows - 1 and c == cols - 1):
                return 1
            
            if((r,c) in cache):
                return cache[(r,c)]
            
            cache[(r,c)] = bfs(r+1,c,cache) + bfs(r,c+1,cache)
            return cache[(r,c)]
        
        return bfs(0,0,cache)

        