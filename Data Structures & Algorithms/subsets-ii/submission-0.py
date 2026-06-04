class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        currSet = []
        subsets = set()
        self.helper(0, currSet, subsets, nums)
        return [list(i) for i in subsets]

    def helper(self,start, currSet, subsets, nums):

        if(start >= len(nums)):
            subsets.add(tuple(currSet))
            return
        
        currSet.append(nums[start])
        self.helper(start + 1, currSet, subsets, nums)
        currSet.pop()
        self.helper(start + 1, currSet, subsets, nums)

        return 

        
        

        