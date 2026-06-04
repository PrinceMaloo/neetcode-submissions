class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dfs(0,0,m,n)  

    def dfs(self,r,c,rows,cols):
        if min(r,c) < 0 or r >= rows or c >= cols:
            return 0
        
        if(r == rows - 1 and c == cols - 1):
            return 1
        
        return self.dfs(r+1,c,rows,cols) + self.dfs(r,c+1,rows,cols)

        