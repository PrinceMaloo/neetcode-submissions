import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while(len(stones) > 1):
            val1 = -heapq.heappop(stones)
            val2 = -heapq.heappop(stones)
            diff = val1 - val2
            if(diff):
                val = -diff
                heapq.heappush(stones,val)
        
        return -1*stones[0] if len(stones) > 0 else 0



        