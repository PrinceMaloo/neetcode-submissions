import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointToDistance = {}
        distanceList = []
        result = []

        for point in points:
            dist = self.calculateDistance(point[0],point[1])
            distanceList.append(dist)
            pointToDistance[tuple(point)] = dist

        heapq.heapify(distanceList)
        while(k > 0):
            resultDist = heapq.heappop(distanceList)
            for (key,val) in pointToDistance.items():
                if(val == resultDist):
                    result.append(list(key))
                    pointToDistance.pop(key)
                    break

            k -= 1
               
        return result
        
    def calculateDistance(self,x,y):
        return x**2 + y**2
        