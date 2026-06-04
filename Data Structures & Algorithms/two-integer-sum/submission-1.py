class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}
        for (index,num) in enumerate(nums):
            diff = target - num 
            if(diff in HashMap):
                return [HashMap[diff],index]

            if(num not in HashMap):
                HashMap[num] = index
        



        



        