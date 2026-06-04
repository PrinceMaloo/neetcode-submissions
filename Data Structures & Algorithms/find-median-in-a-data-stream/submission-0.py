import heapq

class MedianFinder:

    def __init__(self):
        self.smallNumberMaxHeap,self.largerNumberMinHeap = [], []       

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallNumberMaxHeap,-1*num)
        if(self.smallNumberMaxHeap and self.largerNumberMinHeap and -1*self.smallNumberMaxHeap[0] > self.largerNumberMinHeap[0]):
            val = -1*heapq.heappop(self.smallNumberMaxHeap)
            heapq.heappush(self.largerNumberMinHeap,val)
        
        #handle uneven length
        if(len(self.smallNumberMaxHeap) > len(self.largerNumberMinHeap) + 1):
            val = -1*heapq.heappop(self.smallNumberMaxHeap)
            heapq.heappush(self.largerNumberMinHeap,val)
     
        if(len(self.largerNumberMinHeap) > len(self.smallNumberMaxHeap) + 1):
            val = heapq.heappop(self.largerNumberMinHeap)
            heapq.heappush(self.smallNumberMaxHeap,-1*val)     

    def findMedian(self) -> float:
        if(len(self.largerNumberMinHeap) > len(self.smallNumberMaxHeap)):
            return self.largerNumberMinHeap[0]

        elif(len(self.smallNumberMaxHeap) > len(self.largerNumberMinHeap)):
            return -1*self.smallNumberMaxHeap[0]
        
        else:
            return (self.largerNumberMinHeap[0] + -1*self.smallNumberMaxHeap[0])/2

        
        