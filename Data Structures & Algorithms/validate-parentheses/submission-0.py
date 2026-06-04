class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'}': '{', ')':'(', ']':'['}
        openPara = set(['(', '[','{'])

        for val in s:
            if(val in openPara):
                stack.append(val)

            if(val in dict.keys()):
                if(len(stack) == 0):
                    return False

                top = stack.pop()

                if(top != dict[val]):
                    return False

        if(len(stack) != 0):
            return False
            
        return True

        