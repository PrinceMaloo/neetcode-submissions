class MinHeap:
    
    def __init__(self):
        self.array = []
        

    def push(self, val: int) -> None:      
        
        self.array.append(val)
        index = len(self.array)-1
        parentIndex = (index - 1)//2
        while(parentIndex >= 0 and self.array[parentIndex] > self.array[index]):
            temp = self.array[index]
            self.array[index] = self.array[parentIndex]
            self.array[parentIndex] = temp
            index = parentIndex
            parentIndex = (index - 1)//2
        
    def pop(self) -> int:
        if len(self.array) == 0:
            return -1
        
        if len(self.array) == 1:
            return self.array.pop()
        
        res = self.array[0]
        self.array[0] = self.array.pop()
        i = 0
        n = len(self.array)
        leftChildIndex = 2*i + 1
        rightChildIndex = 2*i + 2

        
        if(leftChildIndex < n and rightChildIndex < n):
            (mini,miniIndex) = (self.array[leftChildIndex],leftChildIndex) if self.array[leftChildIndex] < self.array[rightChildIndex]  else (self.array[rightChildIndex],rightChildIndex)                             
        elif leftChildIndex < n:
            (mini,miniIndex) = (self.array[leftChildIndex],leftChildIndex)
        else:
            return res

        while(self.array[i] > mini):
            temp = self.array[i]
            self.array[i] = mini
            self.array[miniIndex] = temp
            i = miniIndex
            leftChildIndex = 2*miniIndex + 1
            rightChildIndex = 2*miniIndex + 2

            print("miniIndex",miniIndex)
            print("self.array",self.array)
            print("leftChildIndex",leftChildIndex)
            print("n",n)

            

            if(leftChildIndex < n and rightChildIndex < n):
                (mini,miniIndex) = (self.array[leftChildIndex],leftChildIndex) if self.array[leftChildIndex] < self.array[rightChildIndex]  else (self.array[rightChildIndex],rightChildIndex)                             
            elif leftChildIndex < n:
                (mini,miniIndex) = (self.array[leftChildIndex],leftChildIndex)
            else:
                break
            
            
        
        return res

    def top(self) -> int:
        if len(self.array) == 0:
            return -1
        
        return self.array[0]
        
    def heapify(self, nums: List[int]) -> None:
        index =(len(nums)//2)-1 if len(nums)%2 else (len(nums)//2)
        
        while(index >= 0):
            
            parentIndex = (index-1) // 2

            while(parentIndex >= 0 and nums[parentIndex] > nums[index]):
                temp = nums[index]
                nums[index] = nums[parentIndex]
                nums[parentIndex] = temp
            
            temp = index
            miniIndex = index
            leftChildIndex = 2*temp + 1
            rightChildIndex = 2*temp + 2
            mini = 0
            n = len(nums) 
            if(leftChildIndex < n and rightChildIndex < n):
                (mini,miniIndex) = (nums[leftChildIndex],leftChildIndex) if nums[leftChildIndex] < nums[rightChildIndex]  else (nums[rightChildIndex],rightChildIndex)                             
            elif leftChildIndex < n:
                (mini,miniIndex) = (self.array[leftChildIndex],leftChildIndex)
            else:
                self.array = nums
                return

            while(nums[temp] > mini):
                

                val = nums[temp]
                nums[temp] = mini
                nums[miniIndex] = val
                temp = miniIndex
                leftChildIndex = 2*miniIndex + 1
                rightChildIndex = 2*miniIndex + 2
                if(leftChildIndex < n and rightChildIndex < n):
                    (mini,miniIndex) = (nums[leftChildIndex],leftChildIndex) if nums[leftChildIndex] < nums[rightChildIndex]  else (nums[rightChildIndex],rightChildIndex)                             
                elif leftChildIndex < n:
                    (mini,miniIndex) = (self.array[leftChildIndex],leftChildIndex)
                else:
                    break
            
            index -= 1
            
        self.array = nums

                
                
                
                
                


            
            
            
            
                



        
        