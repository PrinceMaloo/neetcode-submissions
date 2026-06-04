class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combinations = []
        currCombinations = []
        self.helper(1, n ,k, combinations, currCombinations)
        return combinations
    
    def helper(self, start, n,k, combinations, currCombinations):

        if(len(currCombinations) == k):
            combinations.append(currCombinations.copy())
            return
        if(start > n):
            return 

        currCombinations.append(start)
        self.helper(start + 1, n ,k, combinations, currCombinations)
        currCombinations.pop()
        self.helper(start + 1, n ,k, combinations, currCombinations)
        return 
        



    
        