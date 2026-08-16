class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()     

    def findMedian(self) -> float:
        length = len(self.nums)
        mid = length // 2
        if length % 2:
            return self.nums[mid] 
        else:
            return (self.nums[mid] + self.nums[mid - 1]) / 2

        
        