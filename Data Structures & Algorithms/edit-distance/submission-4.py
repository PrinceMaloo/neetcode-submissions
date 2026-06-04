class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = {}

        def dfs(i,j):
            if i == m:
                return n - j
            
            if j == n:
                return m-i

            if word1[i] == word2[j]:
                return dfs(i+1,j+1)
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            result = min(dfs(i+1,j), dfs(i, j+1))
            result = min(result, dfs(i+1,j+1))
            dp[(i,j)] = result + 1
            return dp[(i,j)]
        
        return dfs(0,0)