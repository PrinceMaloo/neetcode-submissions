class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        globalMin, globalMax = nums[0],nums[0]
        currMax = 0
        currMin = 0
        total = 0

        for n in nums:
            currMax = max(n, currMax + n)
            currMin = min(n, currMin + n)
            
            globalMax = max(globalMax,currMax)
            globalMin = min(globalMin,currMin)
            total += n

        print(globalMax)
        print(globalMin)
        if(globalMax < 0):
            return globalMax

        return max(total-globalMin,globalMax)
        





