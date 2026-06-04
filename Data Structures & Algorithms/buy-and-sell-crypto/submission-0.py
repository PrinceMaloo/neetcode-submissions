class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        resultant = 0
        n = len(prices)
        curr = prices[0]

        if(n == 0 or n==1):
            return resultant
            

        for i in range(1,n):
            diff = prices[i] - curr
            if(diff < 0):
                curr = prices[i]
            else:
                resultant = max(resultant, diff)
        
        return resultant


        