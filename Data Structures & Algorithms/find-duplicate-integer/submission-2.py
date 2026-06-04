class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(1,len(nums)):
            cnt = 0
            for num in nums:
                if num == i:
                    cnt += 1
            
            if(cnt > 1):
                return i
                
                    

        