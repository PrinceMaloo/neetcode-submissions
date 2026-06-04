class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        cache = [[0]*(len(word2) + 1) for i in range(len(word1) + 1)]

        for i in range(len(word1)+1):
            cache[i][-1] = m - i
     
        for j in range(len(word2)+1):
            cache[-1][j] = n - j

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j+1], cache[i+1][j], cache[i][j+1])
        
        return cache[0][0]
