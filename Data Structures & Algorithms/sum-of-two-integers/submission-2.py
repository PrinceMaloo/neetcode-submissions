class Solution:
    def getSum(self, a: int, b: int) -> int:    
        mask = 0xffff
        while (mask&b):
            a, b = a ^ b, (a & b) << 1

        print(bin(a), bin(a*mask))
        return a&mask if b > 0 else a
            