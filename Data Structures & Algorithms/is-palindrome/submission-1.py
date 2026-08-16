class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.validCharacter(s[l]):
                l += 1
                continue
            
            while l < r and not self.validCharacter(s[r]):
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
    
    def validCharacter(self, char):
        if ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'):
            return True

        return False  
        