class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, currSum, currList):
            if(currSum == target):
                res.append(currList.copy())
                return 
            
            if(currSum > target or i >= len(candidates)):
                return
            
            currList.append(candidates[i])
            dfs(i+1,currSum + candidates[i],currList)
            currList.pop()
            while(i+1 < len(candidates) and candidates[i] == candidates[i+1]):
                i+=1
            dfs(i+1,currSum,currList)
            return
        
        dfs(0,0,[])
        return res
        