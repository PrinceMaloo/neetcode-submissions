class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(len(nums)):
            subResult = 1
            for j in range(i,len(nums)):
                subResult *= nums[j]
                result = max(subResult,result) 
            
        return result
