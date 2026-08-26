class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adjacency_list = defaultdict(list)
        cnt = 0

        for src, dist in edges:
            adjacency_list[src].append(dist)
            adjacency_list[dist].append(src)

        def dfs(i):
            if i in visit:
                return
            
            visit.add(i)
            for neigh in adjacency_list[i]:
                dfs(neigh)
            
            return

        for i in range(n):
            if i not in visit:
                cnt += 1
                dfs(i)
        
        return cnt
        
        
        