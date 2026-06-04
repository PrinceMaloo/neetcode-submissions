class Solution:
    def reverse(self, x: int) -> int:
        left, right = -2**31 , 2**31 - 1
        result = []
        answer = 0
        positive = True if x >= 0 else False
        x = abs(x)

        while x:
            result.append(x%10)
            x = x//10
        
        factor = len(result) - 1

        for i in result:
            answer += i*(10**factor)
            factor -= 1
        
        if positive and answer <= right:
            return answer
        elif not positive and -answer >= left:
            return -answer
        else:
            return 0

        

        