from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        hash_map = defaultdict(list)
        l, r = 0, 0

        while r < len(s):
            if s[r] in hash_map and hash_map[s[r]][-1] >= l:
                l = hash_map[s[r]].pop() + 1         
            
            hash_map[s[r]].append(r)
            result = max(result, r - l + 1)
            r += 1
        
        return result
            


        