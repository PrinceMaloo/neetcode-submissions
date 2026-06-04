import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for source, destination, cost in flights:
            adj_list[source].append([destination, cost])
        
        min_heap = [[False, 0, -1, src]]
        while min_heap:
            condition, cost, step, pos = heapq.heappop(min_heap)
         
            if pos == dst:
                if condition:
                    return -1
                return cost
            
            
            for dist_pos, dist_cost in adj_list[pos]:               
                heapq.heappush(min_heap, [k < step + 1, dist_cost + cost, step + 1, dist_pos])

        
        return -1



        
