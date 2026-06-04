class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        edges = set()

        for a,b in prerequisites:
            if b not in adj:
                adj[b] = []          
            if a not in adj:
                adj[a] = []
        
            adj[b].append(a)

        def bfs(key):
            queue = deque()
            visit = set()
            queue.append(key)
            visit.add(key)

            while(queue):
                k = queue.popleft()             
                for neighbour in adj[k]:
                    if neighbour == key:
                        return False
                    
                    if neighbour not in visit:
                        queue.append(neighbour)
                        visit.add(neighbour)
            return True

        
        for key in adj:
            if not bfs(key):
                return False
            
        return True

            





        