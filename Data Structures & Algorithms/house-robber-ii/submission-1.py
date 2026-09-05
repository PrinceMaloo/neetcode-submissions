class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0, nums[0]], [0, 0]]
        for i in range(1, len(nums)):
            if i == len(nums) - 1:
                temp2 = dp[1][1]
                dp[1][1] = max(dp[1][1], nums[i] + dp[1][0])
                dp[1][0] = temp2 
                break

            temp1, temp2 = dp[0][1], dp[1][1]
            dp[0][1] = max(dp[0][1], nums[i] + dp[0][0])
            dp[1][1] = max(dp[1][1], nums[i] + dp[1][0])
            dp[0][0], dp[1][0] = temp1, temp2 
        
        return max(dp[0][1], dp[1][1])
        