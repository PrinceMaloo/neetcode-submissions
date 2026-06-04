import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointToDistance = {}
        distanceList = []
        result = []

        for point in points:
            dist = self.calculateDistance(point[0],point[1])
            distanceList.append([dist,point[0],point[1]])

        heapq.heapify(distanceList)
        while(k > 0):
            resultDist = heapq.heappop(distanceList)
            result.append([resultDist[1],resultDist[2]])

            k -= 1
               
        return result
        
    def calculateDistance(self,x,y):
        return x**2 + y**2
        