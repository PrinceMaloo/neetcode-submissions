class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        visit = set()
        result = []
        def dfs(r, c, prev):
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visit:
                return
            
            result.append(matrix[r][c])
            visit.add((r,c))

            if prev == "right":
                dfs(r,c+1, "right")
                dfs(r+1,c, "down")
            elif prev == "left":
                dfs(r, c-1, "left")
                dfs(r-1, c, "up")
            elif prev == "up":
                dfs(r-1, c, "up")
                dfs(r,c+1, "right")
            else:
                dfs(r+1,c, "down")
                dfs(r, c-1, "left")
            return
        
        dfs(0,0, "right")
        return result
            




        
        


        