class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def minCoinsRequired(index,amount):
            if amount == 0:              
                return 0
            
            if index == len(coins):
                return float("inf")
            
            if (index,amount) in dp:
                return dp[(index,amount)] 
            
            #Exclude         
            exclude = minCoinsRequired(index + 1,amount)
            
            #Include
            include = float("inf")
            if(amount - coins[index] >= 0):
                nextAmount = amount - coins[index]
                include = 1 + minCoinsRequired(index ,nextAmount)
            
            dp[(index,amount)]  = min(exclude,include)
            return dp[(index,amount)]
        
        result = minCoinsRequired(0,amount)
        if result == float("inf"):
            return -1
        return result
            
        