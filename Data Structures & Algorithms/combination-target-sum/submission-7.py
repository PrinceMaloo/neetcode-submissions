class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        resultant = set()

        def dfs(i, val, result):
            if val == 0:
                resultant.add(result)
                return
            
            if val < 0 or i >= len(nums):
                return 
            
            if i + 1 < len(nums):
                dfs(i + 1, val, result)

            dfs(i, val - nums[i], result + (nums[i], ))

        dfs(0, target, tuple())
        resultant = [list(ele) for ele in resultant]
        return resultant