import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        src_cost = 0
        
        for (source, destination, cost) in edges:
            if source == src and destination == src:
                src_cost = cost

            adj[source].append([destination, cost])
        
        
        min_heap = [[0, src]]
        shortest = {}

        while min_heap:
            cost, source = heapq.heappop(min_heap)
            if source in shortest:
                continue
            
            shortest[source] = cost
            for (dist, cost2) in adj[source]:
                if dist not in shortest:
                    heapq.heappush(min_heap, [cost + cost2, dist])
        
        shortest[src] = src_cost

        for node in range(n):
            if node not in shortest:
                shortest[node] = -1

        return shortest

