class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def dfs(i):
            if i >= len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            if i in dp:
                return dp[i]

            cnt = dfs(i+1)
            if i + 1 < len(s) and self.isvalid(s[i] + s[i+1]):
                cnt += dfs(i + 2)

            dp[i] = cnt
            return cnt
        
        return dfs(0)
    
    def isvalid(self, string):
        if 10 <= int(string) <= 26:
            return True
        
        return False