class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + '#'
            result += string
        
        return result

    def decode(self, s: str) -> List[str]:
        print("s",s )
        string_length = -1
        result = []
        i = 0
        prev = ''
        while i < len(s):
            if s[i] == '#':
                string_length = int(prev)  
                prev = ''  
            else:
                prev += s[i]
            
            if string_length != -1:
                string = s[i+1: i + string_length + 1]
                result.append(string)
                i += string_length
                string_length = -1
            
            i += 1
        
        return result

