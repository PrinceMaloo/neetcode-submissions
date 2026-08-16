class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums = list(set(nums))
        nums.sort()

        result = 1
        sub_result = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                sub_result += 1
            else:
                sub_result = 1
            
            result = max(result, sub_result)
        
        return result
