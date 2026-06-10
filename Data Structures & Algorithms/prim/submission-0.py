import heapq

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for (src, dist, w) in edges:
            adj[src].append([dist,w])
            adj[dist].append([src,w])
        
        result = 0
        src = edges[0][0]
        visit = set()
        visit.add(src)
        min_heap = []
        for (dist, w) in adj[src]:
            heapq.heappush(min_heap, [w, src, dist])
        
        while(len(visit) < n and min_heap):
            weight, n1, n2 = heapq.heappop(min_heap)

            if n2 in visit:
                continue

            result += weight
            visit.add(n2)
            for neigh, weight in adj[n2]:
                if neigh not in visit:
                    heapq.heappush(min_heap, [weight, n2, neigh])
            
        return result if len(visit) == n else -1




