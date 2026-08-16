from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        set_t = set(t)
        l, result = 0, None
        for r in range(len(s)):
            if s[r] in set_t:
                count[s[r]] -= 1

            print('count', count)

            while self.ValidSubstring(count) and l <= r:
                if result is None:
                    result = [l,r]
                else:
                    result = result if (result[1]-result[0] < r-l) else [l, r]

                if s[l] in set_t:
                    count[s[l]] += 1
                l += 1

        return s[result[0]:result[1]+1] if result else ""
                    
                
    def ValidSubstring(self, count):
        for val in count.values():
            if val > 0:
                return False
        
        return True
                



        
                




        