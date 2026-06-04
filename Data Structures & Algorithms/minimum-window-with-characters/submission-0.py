class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
         
        min_substring, min_substring_length = "", float("inf")

        for i in range(m):
            substring = ""
            counter = defaultdict(int)
            for k in range(n): 
                counter[t[k]] += 1

            for j in range(i, m):
                substring += s[j]
                if s[j] in counter and counter[s[j]] > 0:
                    counter[s[j]] -= 1
                
                if sum(counter.values()) == 0 and len(substring) < min_substring_length:
                    min_substring = substring
                    min_substring_length = len(substring)
            
        return "" if min_substring_length == float("inf") else min_substring




        