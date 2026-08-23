from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Cycle detection 
        adjacency_list = defaultdict(list)

        for n1, n2 in prerequisites:
            adjacency_list[n1].append(n2)
        
        visit = set()
        for i in range(numCourses):
            cycle = set()
            if self.dfs(i, visit, cycle, adjacency_list):
                return False
            
        return True
    
    def dfs(self, node, visit, cycle, adjacency_list):
        if node in cycle:
            return True
        
        if node in visit:
            return False
        
        visit.add(node)
        cycle.add(node)

        for neighbour in adjacency_list[node]:
            if self.dfs(neighbour, visit, cycle, adjacency_list):
                return True
            
        cycle.remove(node)
            
        return False


        