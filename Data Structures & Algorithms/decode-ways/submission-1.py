class Solution:
    def numDecodings(self, s: str) -> int:
        first, second = 1, 0


        def isvalid(string):
            if 10 <= int(string) <= 26:
                return True
            
            return False

        for i in range(len(s)- 1, -1,-1):
            temp = first

            if s[i] == '0':
                first = 0
            elif i + 1 < len(s) and isvalid(s[i]+s[i+1]):
                first += second
            
            second = temp
        
        return first
