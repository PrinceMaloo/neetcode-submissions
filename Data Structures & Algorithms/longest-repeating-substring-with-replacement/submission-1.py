class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        string_set = set(s)

        for ch in string_set:
            for i in range(0, len(s)):
                cnt, replacement = 0, k
                for j in range(i, len(s)):
                    if s[j] == ch:
                        cnt += 1
                    elif replacement > 0:
                        replacement -= 1
                        cnt += 1
                    else:
                        break
                
                result = max(result, cnt)
        
        return result
        