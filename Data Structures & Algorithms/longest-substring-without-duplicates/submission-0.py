class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for i in range(0, len(s)):
            string_set = set()
            for j in range(i, len(s)):
                if s[j] in string_set:
                    break
                
                string_set.add(s[j])
            
            result = max(result, len(string_set))
        
        return result


        