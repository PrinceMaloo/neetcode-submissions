class Solution:

    def findSubarrayMax(self, nums: List[int], start, end) -> int:

        # larSum = nums[0]
        # currSum = 0
        # for n in nums:
        #     if(currSum < 0):
        #         currSum = 0
            
        #     currSum += n
        #     larSum = max(currSum,larSum)

        # return larSum
        cnt = 0
        L = start
        R = start
        larSum = nums[start]
        currSum = 0
        n = len(nums)

        while(cnt < n):
            if(currSum< 0):
                currSum = 0
            
            currSum += nums[R]
            larSum = max(currSum, larSum)
            R = (R+1)%n
            cnt += 1

        return larSum




    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        larSum = nums[start]
        currSum = 0

        for i in range(n):
            currSum = self.findSubarrayMax(nums,start,end)
            larSum = max(currSum,larSum)
            start += 1
            end = (end+1)%n

        return larSum




