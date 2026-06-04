class MinStack:

    def __init__(self):
        self.stack = []
        self.mini_stack = [ ]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mini_stack:
            self.mini_stack.append(val)
        else:
            self.mini_stack.append(min(self.mini_stack[-1],val))


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.mini_stack.pop()


    def top(self) -> int:
        if(self.stack):
            return self.stack[-1]

    def getMin(self) -> int:  
        if(self.mini_stack):
            return self.mini_stack[-1]
        
