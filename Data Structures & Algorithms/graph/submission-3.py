from collections import deque

class Graph:
    
    def __init__(self):
        self.adjacency_list = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self.adjacency_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if not self.hasPath(src, dst):
            return False
        
        self.adjacency_list[src].discard(dst) 
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.adjacency_list:
            return False
        
        visit, queue = set([src]), deque([src])

        while queue:
            node = queue.popleft()
            if node == dst:
                return True
            
            for connected_node in self.adjacency_list[node]:
                if connected_node not in visit:
                    queue.append(connected_node)
                    visit.add(connected_node)
        
        return False

