from collections import defaultdict 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp, result = defaultdict(int), []

        def dfs(i, amount):
            if i >= len(coins):
                return float("inf")

            if amount == 0:
                return dp[(i-1, amount)]
            if (i, amount) in dp:
                return dp[(i, amount)]

            result = dfs(i+1, amount)
            if amount - coins[i] >= 0:
                result = min(result, 1 + dfs(i, amount - coins[i]))
            
            dp[(i, amount)] = result
            return dp[(i, amount)]
            
            
        result = dfs(0, amount)
        return -1 if result == float("inf") else result
        

        