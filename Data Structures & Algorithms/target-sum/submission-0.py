class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def dfs(index, current_sum):
            if index == n and current_sum == target:
                return 1
            
            if index >= n:
                return 0
            
            if (index, current_sum) in dp:
                return dp[(index,current_sum)]

            result = 0

            result += dfs(index+1,current_sum - nums[index]) + dfs(index+1,current_sum + nums[index])
            dp[(index,current_sum)] = result 
            return dp[(index,current_sum)]
        
        return dfs(0, 0)
        