class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        currMin,currMax = 1,1
        for num in nums:
            temp = currMax * num
            currMax = max(temp,currMin*num,num)
            currMin = min(temp,currMin*num,num)
            result = max(result,currMax)
        
        return result