class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp, result, max_length = [[False]*len(s) for j in range(len(s))], "", -float("inf")

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                flag = True
                if j - i > 2:
                    flag = dp[i+1][j-1]
                
                dp[i][j] = flag and s[i] == s[j]
                if dp[i][j] and j - i + 1 > max_length:
                    max_length, result = j - i + 1, s[i:j+1]
        
        return result
                    

    