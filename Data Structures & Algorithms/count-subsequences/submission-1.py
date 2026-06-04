class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(index, substring):
            if len(substring) == len(t):
                if substring == t:
                    return 1
                return 0
            
            if index > len(s):
                return 0
            
            if (index, substring) in dp:
                return dp[(index, substring)]

            #exclude
            cnt = dfs(index + 1, substring)

            #include 
            if index < len(s) and len(substring) < len(t):  
                cnt += dfs(index + 1, substring + s[index])
            
            dp[(index, substring)] = cnt
            return dp[(index, substring)]
        
        return dfs(0, "")
            




            