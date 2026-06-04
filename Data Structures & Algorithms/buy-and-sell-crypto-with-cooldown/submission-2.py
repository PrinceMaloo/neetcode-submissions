class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(index, buying):
            if index >= len(prices):
                return 0
            
            if (index, buying) in dp:
                return dp[(index, buying)]
            
            cooldown = dfs(index + 1, buying)

            if buying:
                dp[(index, buying)] = max(cooldown, dfs(index + 1, not buying) - prices[index])
            else:
                dp[(index, buying)] = max(cooldown, dfs(index + 2, not buying) + prices[index])
            
            return dp[(index, buying)]
            
            
        return dfs(0,True)
            

            
        