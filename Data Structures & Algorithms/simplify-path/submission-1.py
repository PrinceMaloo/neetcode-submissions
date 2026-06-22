class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ['']
        path = path + '/'
        i, j = 0, 0

        while j < len(path):
            if (path[j] == '/'):
                element = path[i+1:j]
                if element == '..' and len(stack) > 1:
                    stack.pop()
                elif element not in ['.', '..', '']:
                    stack.append(element)
                else:
                    pass
                    
                i = j
         
            j += 1
        
        print("stack", stack)
        result = '/' if len(stack) == 1 else '/'.join(stack) 
        return result
        



            
            


        
