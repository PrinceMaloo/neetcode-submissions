class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(i):
            if i >= len(s):
                return True
            
            if i in dp:
                return dp[i]
            for word in wordDict:
                word_length = len(word)
                if s[i:i + word_length] == word:
                    if dfs(i+word_length):
                        dp[i] = True
                        return True
            
            dp[i] = False
            return dp[i]
        
        return dfs(0)