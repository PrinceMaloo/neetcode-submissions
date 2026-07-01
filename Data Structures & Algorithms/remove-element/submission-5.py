class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = 0
        for (i, num) in enumerate(nums):
            if num != val:
                nums[result] = nums[i]
                result += 1
        
        return result
                