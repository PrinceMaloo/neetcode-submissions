import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxi = max(stones)
        stones = [maxi-i for i in stones]
        heapq.heapify(stones)
        while(len(stones) > 1):
            val1 = -1*(heapq.heappop(stones) - maxi)
            val2 = -1*(heapq.heappop(stones) - maxi)
            diff = val1 - val2
            if(diff):
                val = maxi - diff
                heapq.heappush(stones,val)
        
        return -1*(stones[0]-maxi) if len(stones) > 0 else 0



        