class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        L = 0
        n = len(nums)
        currentSum = 0
        ans = 0

        for R in range(n):
            currentSum += nums[R]
            while(currentSum >= target):
                if(ans == 0):
                    ans = R-L+1
                else:
                    ans = min(ans,R-L+1)
                print("currentSum",currentSum)
                currentSum -= nums[L]
                L += 1
          
        return ans
            

                

        