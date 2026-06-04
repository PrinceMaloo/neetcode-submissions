import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        
        for s,d,t in times:
            adj[s].append([d,t])
        
        heap = [[0,k]]
        shortest = {}
        while(heap):
            t,node = heapq.heappop(heap)

            if node in shortest:
                continue
            
            shortest[node] = t

            for src,dt in adj[node]:
                if src not in shortest:
                    heapq.heappush(heap,[t + dt,src])
        
        return max(shortest.values()) if(len(shortest) == n) else -1
            
        

        
        