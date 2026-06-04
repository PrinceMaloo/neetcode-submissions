class Solution:
    def numDecodings(self, s: str) -> int:  

        def dfs(i):
            if(i == len(s)):
                return 1
            if(not self.isValidString(s[i])):
                return 0
            
            res = dfs(i + 1)

            if(i + 1 < len(s) and self.isValidString(s[i:i+2])):
                res += dfs(i + 2)

            return res

        return dfs(0)             

    def isValidString(self,s):
        if(len(s) == 1 and s == '0'):
            return False
        if(len(s) == 2 and (int(s) < 10 or int(s) > 26)):
            return False
        
        return True

         
        