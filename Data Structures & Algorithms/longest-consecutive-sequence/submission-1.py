class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) <= 1):
            return len(nums)

        nums.sort()
        ans = 1
        currentCon = 1

        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]+1):
                currentCon += 1
                ans = max(ans,currentCon) 
            elif(nums[i]==nums[i-1]):
                continue
            else:
                currentCon = 1

        return ans

        