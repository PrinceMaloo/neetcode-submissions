class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        dp = [[0]*(n+1) for i in range(capacity + 1)]

        for i in range(capacity-1, -1, -1):
            for j in range(n-1,-1,-1):
                dp[i][j] = dp[i][j+1]
                if capacity - i - weight[j] >= 0:
                    dp[i][j] = max(dp[i][j], profit[j] + dp[weight[j] + i][j+1])
                
        return dp[0][0]