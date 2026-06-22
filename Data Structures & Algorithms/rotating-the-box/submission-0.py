class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        rotatedBox = [['.']*m for i in range(n)]

        for r in range(m):
            for c in range(n):
                rotatedBox[c][m-r-1] = boxGrid[r][c]
        
        for c in range(m):
            empty_position = -1 
            for r in range(n-1, -1, -1): 
                if rotatedBox[r][c] == '.' and empty_position == -1:
                    empty_position = r
                elif rotatedBox[r][c] == '#' and empty_position != -1:
                    rotatedBox[r][c], rotatedBox[empty_position][c] = rotatedBox[empty_position][c], rotatedBox[r][c]
                    empty_position = empty_position - 1
                elif rotatedBox[r][c] == '*':
                    empty_position = -1
                else:
                    continue
                

        
        # for r in range(n-2, -1, -1):
        #     empty_position = -1
        #     for c in range(m):
        #         if rotatedBox[r][c] == '.':
        #             empty_position = r if empty_position != -1 else 
        #         if rotatedBox[r][c] == '#' and rotatedBox[r+1][c] == '.':
        #             rotatedBox[r][c], rotatedBox[r+1][c] =  rotatedBox[r+1][c], rotatedBox[r][c]
        
        return rotatedBox


        