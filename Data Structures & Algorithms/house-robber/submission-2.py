class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]

        first,second = nums[0],max(nums[1],nums[0])

        for i in range(2,len(nums)):
            temp = second
            second = second + nums[i] if(second - first == 0) else max(first + nums[i],second)
            first = temp
        
        return second

                
                


