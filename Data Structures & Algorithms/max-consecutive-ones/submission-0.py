class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
                result = max(result,cnt)      
            else:
                cnt = 0

        return result
        