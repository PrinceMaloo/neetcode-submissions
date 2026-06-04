class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def minCost(index,cache):
            if(index == 0 or index == 1):
                return 0
             
            if index in cache:
                return cache[index]
            
            cache[index]  = min(cost[index-1] + minCost(index-1,cache), cost[index-2] + minCost(index-2,cache))
            return cache[index]
        
        return minCost(len(cost),cache)




        