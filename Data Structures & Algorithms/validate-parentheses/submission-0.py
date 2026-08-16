class Solution:
    def isValid(self, s: str) -> bool:
        map = {'}': '{', ')': '(', ']' : '['}
        openbracket_set = set(['(', '[', '{'])
        stack = []
        for i in range(len(s)):
            if s[i] in openbracket_set:
                stack.append(s[i])
            else:
                if not stack or stack.pop() != map[s[i]]:
                    return False
                
        return True if len(stack) == 0 else False
                



