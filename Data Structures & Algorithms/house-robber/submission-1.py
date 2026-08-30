class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]

        for i in range(len(nums)):
            temp = max(dp[0], dp[1])
            dp[0] = nums[i] + dp[1]
            dp[1] = temp

        return max(dp)