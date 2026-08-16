import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        diff = len(self.max_heap) - len(self.min_heap)
        
        if not self.max_heap:
            self.max_heap.append(-num)
            return 
       
        if diff == 1:
            if num >= -self.max_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                max_heap_top = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, max_heap_top)
                heapq.heappush(self.max_heap, -num)
        else:      
            if num <= self.min_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                min_heap_top = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -min_heap_top)
                heapq.heappush(self.min_heap, num)

    def findMedian(self) -> float:
        diff = len(self.max_heap) - len(self.min_heap)
        if diff != 0:
            return -self.max_heap[0]
        
        return (-self.max_heap[0] + self.min_heap[0]) / 2      
        