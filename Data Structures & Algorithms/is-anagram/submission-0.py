from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_map1 = Counter(t)
        hash_map2 = Counter(s)

        for key in hash_map1:
            if key not in hash_map2:
                return False

            if hash_map1[key] != hash_map2[key]:
                return False
        
        return True
        