class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        n = len(self.array)
        if (i < n):
            return self.array[i]
        return -1

    def set(self, i: int, n: int) -> None:
        length = len(self.array)
        if(i < length):
            self.array[i] = n 

    def pushback(self, n: int) -> None:
        length = len(self.array)
        if length == self.capacity:
            self.resize()
        
        self.array.append(n)
        
    def popback(self) -> int:
        return self.array.pop()

    def resize(self) -> None:
        self.capacity = self.capacity*2

    def getSize(self) -> int:
        return len(self.array)
          
    def getCapacity(self) -> int:
        return self.capacity
