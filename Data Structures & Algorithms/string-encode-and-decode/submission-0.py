class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for str in strs:
            ans += (str + 'İ')
        return ans


    def decode(self, s: str) -> List[str]:
        print("s",s)
        lst = []
        val = ""
        for i in s:    
            if(i == 'İ'):
                lst.append(val)
                val = ""
                continue
            val += i
        return lst
