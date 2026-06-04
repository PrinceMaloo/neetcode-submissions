class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if(n == 0 or n==1):
            return n

        ans = 0
        
        for i in range(n):
            countSet = set()
            for j in range(i,n):
                if(s[j] in countSet):
                    break
                countSet.add(s[j])
                ans = max(ans,j-i+1)
        return ans

        