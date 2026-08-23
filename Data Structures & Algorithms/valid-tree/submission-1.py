from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency_list, visit = defaultdict(list), set()

        for src, dist in edges:
            adjacency_list[src].append(dist)
            adjacency_list[dist].append(src)
        

        if self.dfs(0, -1, visit, adjacency_list):
            return False
        
        for i in range(n):
            if i not in visit:
                return False
        
        return True
    
    def dfs(self, node, parent, visit, adjacency_list):
        if node in visit:
            return False

        visit.add(node)

        for neighbour in adjacency_list[node]:
            if neighbour in visit and neighbour != parent:
                return True
            
            if neighbour not in visit:
                self.dfs(neighbour, node, visit, adjacency_list)
        
        return False

        