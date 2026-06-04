class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        dp = {}
        def dfs(index, current_sum):
            if index == len(nums):
                return total == 2*current_sum 
            
            if (index, current_sum) in dp:
                return dp[(index, current_sum)]
            
            dp[(index, current_sum)] = dfs(index + 1, current_sum) or dfs(index + 1, current_sum + nums[index])
            return dp[(index, current_sum)]
        
        return dfs(0,0)
            
        