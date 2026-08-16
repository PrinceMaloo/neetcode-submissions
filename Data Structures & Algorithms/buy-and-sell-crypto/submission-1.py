class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            profit = max(prices[i] - buy, profit)
            buy  = min(prices[i], buy)
        
        return profit
            