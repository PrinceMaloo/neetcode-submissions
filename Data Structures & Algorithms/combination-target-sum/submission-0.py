class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        globalSet = set()
        currList = []
        self.combinationSums(0,currList,globalSet,nums,target)
        result = [list(i) for i in globalSet]
        return result
    


    def combinationSums(self,currSum, currList, currSet,nums,target):
        if(currSum == target):
            currList.sort()
            currSet.add(tuple(currList))
            return
        if(currSum > target):
            return
        
        for num in nums:
            currSum = currSum + num
            currList.append(num)
            self.combinationSums(currSum,currList.copy(),currSet,nums,target)
            currSum -= num
            currList.pop()
        
        return


        










        
        
        