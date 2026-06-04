import heapq

class UnionFind:
    def __init__(self,n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}
    
    def Find(self,u):
        print(u)
        if(self.parent[u] == u):
            return u
        
        self.parent[u] = self.Find(self.parent[u])
        return self.parent[u]
    
    def Union(self,u,v):
        pu = self.Find(u)
        pv = self.Find(v)

        if(self.rank[pu] < self.rank[pv]):
            self.parent[pu] = pv        
        elif(self.rank[pu] > self.rank[pv]):
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        mst = []
        union = UnionFind(n)

        for u,v,w in edges:
            heapq.heappush(minHeap,(w,u,v))

        while(len(mst) < n - 1 and minHeap):
            w,u,v = heapq.heappop(minHeap)

            if(union.Find(u) == union.Find(v)):
                continue
            
            union.Union(u,v)
            mst.append((u,v,w))
        
        return -1 if len(mst) != n-1 else sum(cost for _,_,cost in mst)

        
        
        


        

