class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(31, -1,-1):
            remainder = n & 1
            n = n >> 1
            result += (remainder* (2**i))
        return result
        



        