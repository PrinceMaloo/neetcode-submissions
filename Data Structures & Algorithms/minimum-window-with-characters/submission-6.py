from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        set_t = set(t)
        l, result, resLen = 0, [-1, -1], float("inf")
        have, need = 0, len(t)

        for r in range(len(s)):
            if s[r] in set_t:
                count[s[r]] -= 1
                if count[s[r]] >= 0:
                    have += 1

            while have == need and l <= r:        
                if (r - l + 1) < resLen:
                    resLen = r-l+1
                    result = [l, r]
                if s[l] in set_t:
                    count[s[l]] += 1
                    if count[s[l]] > 0:
                        have -= 1
                l += 1

        l, r = result
        return "" if resLen == float("inf") else s[l:r+1]
                                 


        
                




        