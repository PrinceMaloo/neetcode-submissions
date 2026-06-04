import math
class Solution:
    def reverse(self, x: int) -> int:
        left, right = -2**31 , 2**31 - 1
        answer = 0
        num = abs(x)

        while num:
            answer += (num%10)*(10**int(math.log10(num)))
            num = num//10
        
        if x >= 0 and answer <= right:
            return answer
        elif x < 0 and -answer >= left:
            return -answer
        else:
            return 0

        

        