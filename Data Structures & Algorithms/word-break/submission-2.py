class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                word_length = len(word)
                if (i + word_length) <= len(s) and s[i: i + word_length] == word:
                    dp[i] = dp[i + word_length]
                    
                if dp[i]:
                    break
        
        return dp[0]
