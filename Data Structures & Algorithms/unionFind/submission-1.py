#There are two ways to do this
#Union by Rank or Union by Height


class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.num_components = n
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
     
    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x
        else:
            return self.find(self.parent[x])
        
    def isSameComponent(self, x: int, y: int) -> bool:
        if self.find(x) == self.find(y):
            return True
        
        return False

    def union(self, x: int, y: int) -> bool:
        p_x = self.find(x)
        p_y = self.find(y)

        if p_x == p_y:
            return False
        
        r_x, r_y = self.rank[p_x], self.rank[p_y]

        if r_x < r_y:
            self.parent[p_x] = p_y
        elif r_x > r_y:
            self.parent[p_y] = p_x
        else:
            self.parent[p_x] = p_y
            self.rank[p_y] += 1
        
        self.num_components -= 1
        return True
        

    def getNumComponents(self) -> int:
        return self.num_components 

