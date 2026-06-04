class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = 0
        resultantString = ""

        def helper(left,right):   
            nonlocal result,resultantString
            while(left >= 0 and right <= len(s)-1 and s[right] == s[left]):
                    if(right - left + 1 > result):
                        result = right - left + 1   
                        resultantString = s[left:right+1]
                    
                    left -= 1
                    right += 1

        for i in range(len(s)):
            helper(i,i)
            helper(i,i+1)

        return resultantString

    