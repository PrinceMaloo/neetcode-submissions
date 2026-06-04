class Solution:
    def isValidParenthesis(self,string):
        stack = []
        for s in string:
            if(s == '('):
                stack.append(s)
            else:
                if(len(stack) == 0):
                    return False
                stack.pop()
        
        return True

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        if(n == 1):
            result.append("()")
            return result
        
        previousResult = self.generateParenthesis(n-1)
        for s in "()":
            subResult = set()
            for (i,res) in enumerate(previousResult):
                for index in range(len(res)+1):
                    subString = res[0:index] + s + res[index:]                   
                    subResult.add(subString)
                
            previousResult = list(subResult)

        for parenthesis in previousResult:
            if(self.isValidParenthesis(parenthesis)):
                result.append(parenthesis)
            
        return result

            
                
        
                    

                        
                    

        