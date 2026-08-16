class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        resultant = set()

        def dfs(i, val, result):
            if val == 0:
                resultant.add(tuple(result))
                return
            
            if val < 0 or i >= len(nums):
                return 
            
            dfs(i + 1, val, result)
            result.append(nums[i])
            dfs(i, val - nums[i], result)
            result.pop()

        dfs(0, target, [])
        resultant = [list(ele) for ele in resultant]
        return resultant
        