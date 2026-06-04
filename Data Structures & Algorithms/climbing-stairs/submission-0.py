class Solution:
    def climbStairs(self, n: int) -> int:
        return self.fibonacci(n+1)
    
    def fibonacci(self,n):
        if(n < 2):
            return n
        
        dp = [0,1]
        i = 2
        while(i<=n):
            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp
            i += 1

        return dp[1]
        