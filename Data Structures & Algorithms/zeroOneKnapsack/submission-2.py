class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        M = capacity
        dp = [0] * (M+1)

        for i in range(M+1):
            if weight[0] <= i:
                dp[i] = profit[0]

        for i in range(1, n, 1):
            curr_row = [0] * (M+1)
            for c in range(1,M+1,1):
                skip = dp[c]
                include = 0

                if c - weight[i] >= 0:
                    include = profit[i] + dp[c - weight[i]]
                
                curr_row[c] = max(skip, include)
            
            dp = curr_row
                
        return dp[M]