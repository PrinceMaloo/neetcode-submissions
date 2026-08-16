class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1
        while l < r:
            left_ch = s[l]
            right_ch = s[r]

            if not self.validCharacter(left_ch):
                l += 1
                continue
            
            if not self.validCharacter(right_ch):
                r -= 1
                continue

            if left_ch.lower() != right_ch.lower():
                return False
            
            l += 1
            r -= 1
        
        return True
    
    def validCharacter(self, char):
        if ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'):
            return True

        return False  
        