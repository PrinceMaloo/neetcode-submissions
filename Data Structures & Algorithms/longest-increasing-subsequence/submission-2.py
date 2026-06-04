class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def dfs(index):
            if index == len(nums):
                return 0
                
            if index in dp:
                return dp[index]
            
            result = 1

            for i in range(index + 1, len(nums)):
                sub_result = dfs(i)
                if nums[index] < nums[i]:
                    result = max(result, 1 + sub_result)
            
            dp[index] = result
            return dp[index]

        result = 0
        for index in range(len(nums)):
            result = max(result, dfs(index))
        
        return result

        