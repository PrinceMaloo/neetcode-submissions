class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        array = [0]*26
        for i in range(len(s)):
            array[ord(s[i]) - ord('a')] += 1
            array[ord(t[i]) - ord('a')] -= 1

        for value in array:
            if value != 0:
                return False
            
        return True
        
        
