class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        currSet = []
        self.helper(0,currSet,subsets,nums)
        return subsets

    def helper(self,start, currSet,subsets,nums):

        if(start == len(nums)):
            subsets.append(currSet.copy())
            return 
        
        currSet.append(nums[start])
        self.helper(start + 1, currSet,subsets, nums)
        currSet.pop()
        self.helper(start + 1, currSet,subsets,nums)
        return 


        