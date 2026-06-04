class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        mini = 1
        maxi = max(piles)
        resultant = maxi

        while(mini <= maxi):
            mid = mini + int((maxi - mini)/2)
            numberHours = self.numberOfHours(piles,mid)
            if(numberHours > h):
                mini = mid + 1
            else:
                resultant = mid
                maxi = mid  - 1
        return resultant 
        
        
            
        
        

    def numberOfHours(self,piles: List[int],rate):
        resultant = 0
        for i in piles:
            resultant += math.ceil(i/rate)
        
        return resultant



            

        