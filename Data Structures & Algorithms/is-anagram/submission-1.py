from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_map1 = defaultdict(int)
        hash_map2 = defaultdict(int)

        for i in range(len(s)):
            hash_map1[s[i]] += 1
            hash_map2[t[i]] += 1

        for key in hash_map1:
            if key not in hash_map2:
                return False

            if hash_map1[key] != hash_map2[key]:
                return False
        
        return True
        