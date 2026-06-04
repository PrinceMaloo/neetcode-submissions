from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False

        adjancy_matrix = defaultdict(list)
        starting_node = 0
        for (k, v) in edges:
            adjancy_matrix[k].append(v)
            adjancy_matrix[v].append(k)

        def bfs(node, parent):
            queue = deque()
            queue.append((node, parent))
            visit = set()
            visit.add(node)

            while(queue):
                node, parent = queue.popleft()
                for neighbour in adjancy_matrix[node]:
                    if neighbour == parent:
                        continue

                    if neighbour in visit:
                        return False
                    
                    queue.append((neighbour, node))
                    visit.add(neighbour)

            return True and len(visit) == n
        
        return bfs(starting_node, -1)



