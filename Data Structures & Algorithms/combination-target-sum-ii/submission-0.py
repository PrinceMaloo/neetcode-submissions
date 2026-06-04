class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        result = set()
        def dfs(i, currSum, currList):
            if(currSum == target):
                res.append(currList.copy())
                return 
            
            if(currSum > target or i >= len(candidates)):
                return
            
            currList.append(candidates[i])
            dfs(i+1,currSum + candidates[i],currList)
            currList.pop()
            dfs(i+1,currSum,currList)
            return
        
        dfs(0,0,[])
        for i in res:
            result.add(tuple(sorted(i)))

        resultant = [list(i) for i in result]
        return resultant
        