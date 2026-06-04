class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {}

        def dfs(index, current_amount):
            if index >= len(coins):
                return 0

            if current_amount == amount:
                return 1
            
            if (index,current_amount) in dp:
                return dp[(index,current_amount)]
            
            
            #Exclude this index
            result = dfs(index + 1, current_amount)

            if current_amount + coins[index] <= amount:
                result += dfs(index, current_amount + coins[index])
            
            dp[(index,current_amount)] = result

            return dp[(index,current_amount)]
        
        return dfs(0,0)


                
            
        