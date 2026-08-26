class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adjacency_list = defaultdict(list)
        cnt = 0

        for src, dist in edges:
            adjacency_list[src].append(dist)
            adjacency_list[dist].append(src)

        for i in range(n):
            if i not in visit:
                queue = deque([i])
                cnt += 1
                while queue:
                    node = queue.popleft()
                    visit.add(node)
                    for neigh in adjacency_list[node]:
                        if neigh not in visit:
                            queue.append(neigh)
        
        return cnt
                
        
        