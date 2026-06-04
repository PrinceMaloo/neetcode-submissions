import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []
        visit = set()
        n = len(points)
        result = 0
        x1 = points[0][0]
        y1 = points[0][1]

        for x,y in points:
            weight = abs(x - x1) + abs(y- y1)
            heapq.heappush(minHeap,[weight,[x1,y1],[x,y]])
        
        visit.add((x1,y1))

        while(len(visit) < n and minHeap):
            
            w,(x1,y1),(x2,y2) = heapq.heappop(minHeap)
            if (x2,y2) in visit:
                continue
            
            result += w
            visit.add((x2,y2))

            for (x,y) in points:
                if (x,y) not in visit:
                    weight = abs(x - x2) + abs(y - y2)
                    heapq.heappush(minHeap,[weight,[x2,y2],[x,y]])
        
        return result
                    
            




        