class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0]*(capacity + 1)
        n = len(profit)

        for c in range(capacity + 1):
            if weight[0] <= c:
                dp[c] = profit[0] + dp[c-weight[0]]
            
        for i in range(1, n,1):
            curr_row = [0]*(capacity + 1)
            for c in range(1, capacity+1, 1):
                skip = dp[c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + curr_row[c - weight[i]]

                curr_row[c] = max(skip, include)
        
            dp = curr_row
        
        return dp[capacity]
