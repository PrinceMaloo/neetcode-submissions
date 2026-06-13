class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = {}
        n = len(profit)

        def dfs(i, current_capacity):
            if i == n or current_capacity < 0:
                return 0
            
            if (i, current_capacity) in dp:
                return dp[(i, current_capacity)]

            #exclude 
            dp[(i, current_capacity)] = dfs(i + 1, current_capacity)

            #include
            if current_capacity - weight[i] >= 0:
                dp[(i, current_capacity)] = max(dp[(i, current_capacity)], 
                                                profit[i] + dfs(i, current_capacity - weight[i]))

            return dp[(i, current_capacity)]
        
        return dfs(0, capacity)
                                                

        
