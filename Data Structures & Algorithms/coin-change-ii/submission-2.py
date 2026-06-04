class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        dp = [[0]*(amount + 1) for i in range(2)]

        for i in range(amount + 1):
            dp[0][i] = 0
        
        for i in range(2):
            dp[i][0] = 1
        
        for i in range(1,n+1,1):
            for j in range(1, amount + 1):
                row = i - 1
                coin = coins[row]
                dp[1][j] = dp[0][j] + (dp[1][j-coin] if j-coin >= 0 else 0)
            
            dp[0] = dp[1].copy()
        return dp[1][amount]

        

                
            
        