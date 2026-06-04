class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}

        for a,b in prerequisites:
            if b not in adj:
                adj[b] = []          
            if a not in adj:
                adj[a] = []
        
            adj[b].append(a)
        
        return self.topologicalSort(adj,numCourses)


    def topologicalSort(self,adj,numCourses):
        topSort = []
        visit = set()
        curr = set()
        for key in adj:
            if not self.dfs(adj,key,visit,topSort,curr):
                return []

        topSort.reverse()
        for num in range(numCourses):
            if num not in topSort:
                topSort.append(num)
            
        return topSort

    def dfs(self,adj,src,visit,topSort,curr):
        if src in curr:
            return False

        if src in visit:
            return True
         
        
        visit.add(src)
        curr.add(src)
        for neigh in adj[src]:         
            if not self.dfs(adj,neigh,visit,topSort,curr):
                return False

        curr.remove(src)
        topSort.append(src)
        return True

        