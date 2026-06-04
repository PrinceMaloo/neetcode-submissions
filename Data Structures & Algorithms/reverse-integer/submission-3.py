import math
class Solution:
    def reverse(self, x: int) -> int:
        left, right = -2**31 , 2**31 - 1
        answer = 0
        num = abs(x)

        while num:
            answer = answer * 10 + num % 10
            num = num//10
        
        if x < 0:
            answer = -answer
        
        return answer if left <= answer <= right else 0
        