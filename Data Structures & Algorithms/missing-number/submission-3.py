class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i, val in enumerate(nums):
            result = result + i - val
        
        return result