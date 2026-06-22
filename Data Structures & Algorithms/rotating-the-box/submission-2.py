class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        rotatedBox = [['.']*m for i in range(n)]

        for r in range(m):
            i = n - 1
            for c in range(n-1,-1,-1):
                if boxGrid[r][c] == '#':
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                    rotatedBox[i][m-r-1] = '#'
                    i -= 1
                elif boxGrid[r][c] == '*':
                    rotatedBox[c][m-r-1] = '*'
                    i = c - 1                 
                else:
                    continue

        
        return rotatedBox


        