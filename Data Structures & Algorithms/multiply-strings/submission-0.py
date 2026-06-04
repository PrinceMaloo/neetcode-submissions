class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        result = 0
        outer_factor = 1
        for i in range(m-1,-1,-1):
            sub_result, inner_factor, carry = 0, 1, 0
            for j in range(n-1, -1,-1):
                value = int(num1[i])*int(num2[j])
                reminder = (carry + value) % 10
                carry = (carry + value) // 10
                sub_result += reminder * inner_factor
                inner_factor *= 10
            
            if carry:
                sub_result += carry * inner_factor
            
            result += sub_result*outer_factor
            outer_factor *= 10
        
        return str(result)
            



        