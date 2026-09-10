class Solution:
    def countSubstrings(self, s: str) -> int:
        dp, cnt = [[False]*len(s) for i in range(len(s))], 0

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                flag = True
                if j - i > 2:
                    flag = dp[i+1][j-1]
                
                dp[i][j] = flag and s[i] == s[j]
                if dp[i][j]:
                    cnt += 1
            
        return cnt