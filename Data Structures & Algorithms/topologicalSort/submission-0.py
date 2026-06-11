class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for (src, dist) in edges:
            adj[src].append(dist)
        
        def dfs(vertice):
            if vertice in visiting:
                return False
            
            if vertice in visit:
                return True
            
            visit.add(vertice)
            visiting.add(vertice)
            for neighbour in adj[vertice]:
                if not dfs(neighbour):
                    return False
            
            visiting.remove(vertice)
            topological_sort.append(vertice)
            return True
            

        visit = set()
        visiting = set()
        topological_sort = []
        for i in range(n):
            if not dfs(i):
                return []
        
        topological_sort.reverse()
        return topological_sort

        
        