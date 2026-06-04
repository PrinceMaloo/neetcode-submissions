class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(index):
            if(index == len(s)):
                return True
            
            if(index in dp):
                return dp[index]
            
            result = False
            for word in wordDict:
                if s[index:index + len(word)] == word:
                    dp[index + len(word)] = dfs(index + len(word))
                    result = result or dp[index + len(word)]
                                    
            dp[index] =  result   
            return dp[index]
            
                 
        return dfs(0)
            
        