import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+','-','*','/'}

        for i in tokens:
            if(i not in operators):
                stack.append(int(i))
            else:
                val2 = stack.pop()
                val1 = stack.pop()

                if(i == '+'):
                    result = val1 + val2 
                    stack.append(result)
                elif(i == '-'):
                    result = val1 - val2 
                    stack.append(result)
                elif(i == '*'):
                    result = val1 * val2 
                    stack.append(result)
                else:
                    result = int(val1 / val2)
                    stack.append(result)

        return (stack.pop())
                
        