class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)-1

        while(L<R):
            ascii_L = ord(s[L])
            ascii_R = ord(s[R])
            
            if(not (48 <= ascii_L <= 57 or  65 <= ascii_L <= 90 or  97 <= ascii_L <= 122)):
                L += 1
                continue
            if(not (48 <= ascii_R <= 57 or  65 <= ascii_R <= 90 or  97 <= ascii_R <= 122)):
                R -= 1
                continue

            if(s[L].lower() != s[R].lower()):
                return False
            L+= 1
            R -= 1
        return True
        

        