class Solution:
    def canJump(self, nums: List[int]) -> bool:   
        if not nums:
            return True

        dp = {}
        def canJumpFromIndex(index):
            if index >= len(nums) - 1:
                return True
            
            if nums[index] == 0:
                return False
            
            if index in dp:
                return dp[index]
            
            res = False
            for i in range(1,nums[index]+1):               
                res = res or canJumpFromIndex(index + i)
            
            dp[index] = res
            return dp[index]
        
        return canJumpFromIndex(0)


        