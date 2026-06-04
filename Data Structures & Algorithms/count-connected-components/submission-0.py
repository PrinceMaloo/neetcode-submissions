class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adjacency_list = defaultdict(list)
        result = 0

        for (src,dist) in edges:
            adjacency_list[src].append(dist)
            adjacency_list[dist].append(src)

        def dfs(n):
            if n in visit:
                return
            
            visit.add(n)

            for next_element in adjacency_list[n]:
                if next_element not in visit:
                    dfs(next_element)
            
            return
        
        for i in range(n):
            if i not in visit:
                dfs(i)
                result += 1
        
        return result


        