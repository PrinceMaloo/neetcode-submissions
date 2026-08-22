class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        result = []

        pacific = set()
        atlantic = set()
        
        for i in range(rows):
            pacific.add((i, 0))
            atlantic.add((i, cols - 1))
        
        for i in range(cols):
            pacific.add((0, i))
            atlantic.add((rows - 1, i))

        def dfs(r, c, sub_result):
            if(min(r, c) < 0 or r == rows or c == cols):
                return

            sub_result.add((r,c))
            neighbours = [[0,1], [0,-1], [1, 0], [-1, 0]]

            for dr,dc in neighbours:
                nr, nc = r + dr, c + dc
                if ((nr,nc) not in sub_result and (0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c])):
                    dfs(nr, nc, sub_result)
                 
            return
        
        for (i, j) in pacific.copy():
            dfs(i,j, pacific)
        
        for (i, j) in atlantic.copy():
            dfs(i, j, atlantic)
        
        for pair in pacific:
            if pair in atlantic:
                result.append(pair)
                
        return result

