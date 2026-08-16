from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        hash_map = {}
        l, r = 0, 0

        while r < len(s):
            if s[r] in hash_map:
                l = max(hash_map[s[r]] + 1, l )   
            
            hash_map[s[r]] = r
            result = max(result, r - l + 1)
            r += 1
        
        return result
            


        