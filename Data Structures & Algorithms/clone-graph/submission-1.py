
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 

        visit = {}
        
        def dfs(node):
            if not node:
                return node
            
            if node.val in visit:
                return visit[node.val]
            
            print(node.val)
            d_node = Node(node.val)
            visit[d_node.val] = d_node
            for neighbour_node in node.neighbors:
                print('neighbour_node', neighbour_node.val)
                if neighbour_node:
                    d_node.neighbors.append(dfs(neighbour_node))
            
            return d_node

        return dfs(node)
                
            

