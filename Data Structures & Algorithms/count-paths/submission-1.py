class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        return self.dfs(0,0,m,n,cache)  

    def dfs(self,r,c,rows,cols,cache):
        if min(r,c) < 0 or r >= rows or c >= cols:
            return 0
        
        if (r,c) in cache:
            return cache[(r,c)]

        if(r == rows - 1 and c == cols - 1):
            return 1
        
        cache[(r,c)] = self.dfs(r+1,c,rows,cols,cache) + self.dfs(r,c+1,rows,cols,cache)
        return cache[(r,c)]

        