class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        
        result = []
        for i in range(1, len(s) + 1):
            substring = s[0:i]
            if(not self.isPalindrome(substring)):
                continue
            
            subproblem_list = self.partition(s[i:]) if i < len(s) else [[]]
            for sub in subproblem_list:
                sub.append(substring)
                result.append(sub)
        
        return result
    
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while(l <= r):
            if(s[l] != s[r]):
                return False
            
            l += 1
            r -= 1
        
        return True        