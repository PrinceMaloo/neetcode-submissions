class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return True
        zerothIndex = None
        zeroFlag = False
        for i in range(len(nums)-1,-1,-1):
            if(zeroFlag and nums[i] >= (zerothIndex)- i):
                if(zerothIndex == len(nums) - 1):
                    zeroFlag = False
                    zerothIndex = None
                elif(nums[i] > (zerothIndex)  - i):
                    zeroFlag = False
                    zerothIndex = None

            if(not zeroFlag and nums[i] == 0):
                zeroFlag = True
                zerothIndex = i

        return not zeroFlag           
            
                    

        