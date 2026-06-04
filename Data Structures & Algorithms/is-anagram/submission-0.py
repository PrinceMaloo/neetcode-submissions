class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)

        if(n1 != n2):
            return False
        
        Hashmap1 = {}
        Hashmap2 = {}

        for i in range(n1):
            if(s[i] in Hashmap1):
                Hashmap1[s[i]] += 1
            else:
                Hashmap1[s[i]] = 1
            if(t[i] in Hashmap2):
                Hashmap2[t[i]] += 1
            else:
                Hashmap2[t[i]] = 1
            
        for char in s:
            if char not in t:
                return False
            if(Hashmap1[char] != Hashmap2[char]):
                return False
            
        return True
        