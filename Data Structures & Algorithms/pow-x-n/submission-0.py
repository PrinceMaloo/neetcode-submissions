class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        result = 1
        for i in range(abs(n)):
            result *= x
        
        return result if n >= 0 else 1/result