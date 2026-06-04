# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        larSum = nums[0]
        currSum = 0

        for n in nums:
            if(currSum < 0):
                currSum = 0
            currSum += n
            larSum = max(currSum,larSum)

        return larSum


            


    