class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = 0
        resultantString = ""
        for i in range(len(s)):
            substring = ""
            for j in range(i,len(s)):
                substring += s[j]
                if(self.isPalindrome(substring)):
                    if(len(substring) >= result):
                         result = len(substring)  
                         resultantString = substring             

        return resultantString

    def isPalindrome(self,s):
        start = 0
        end = len(s)-1
        while(start < end):
            if(s[start] != s[end] ):
                return False
            start += 1
            end -= 1
        
        return True