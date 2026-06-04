class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first,second = 0,0
        for i in range(2,len(cost)+1):
            temp = second
            second = min(second + cost[i-1] , first + cost[i-2])
            first = temp
        
        return second




        