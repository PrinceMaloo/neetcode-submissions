class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        nums.sort()
        for num in nums:
            if (num != i):
                break
             
            i += 1
        
        return i