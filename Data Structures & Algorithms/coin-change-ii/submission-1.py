class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        dp = [[0]*(amount + 1) for i in range(n + 1)]

        for i in range(amount + 1):
            dp[0][i] = 0
        
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1,n+1,1):
            for j in range(1, amount + 1):
                row = i - 1
                coin = coins[row]
                dp[i][j] = dp[i-1][j] + (dp[i][j-coin] if j-coin >= 0 else 0)
            
        return dp[n][amount]

        

                
            
        