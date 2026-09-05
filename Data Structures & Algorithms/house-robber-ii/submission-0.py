class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        def dfs(i, flag):
            if (i == n - 1 and flag) or i >= n:
                return 0
            
            if (i, flag) in dp:
                return dp[(i, flag)]
            
            result = dfs(i+1, flag)
            if i == 0:
                result = max(result, nums[i] + dfs(i+2, not flag))
            else:
                result = max(result, nums[i] + dfs(i+2, flag))
            
            dp[(i, flag)] = result
            return dp[(i, flag)]

        return dfs(0, False)
        