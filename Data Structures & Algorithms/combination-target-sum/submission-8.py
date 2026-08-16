class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        resultant = []

        def dfs(i, val, result):
            if val == 0:
                resultant.append(result.copy())
                return
            
            if val < 0 or i >= len(nums):
                return 
            
            dfs(i + 1, val, result)
            result.append(nums[i])
            dfs(i, val - nums[i], result)
            result.pop()

        dfs(0, target, [])
        return resultant
        