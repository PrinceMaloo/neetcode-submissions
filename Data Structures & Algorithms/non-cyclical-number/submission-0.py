class Solution:
    def isHappy(self, n: int) -> bool:
        flag = set()

        while(True):
            if n in flag:
                return False

            number = n
            sum_value = 0
            while(number):
                remainder = number % 10
                number = math.floor(number / 10)
                sum_value += (remainder)**2     
            
            flag.add(n)
            if(sum_value == 1):
                return True

            n = sum_value
        

