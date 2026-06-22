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
                    i -= 1
                elif boxGrid[r][c] == '*':
                    i = c - 1
                else:
                    continue

        for r in range(m):
            for c in range(n):
                rotatedBox[c][m-r-1] = boxGrid[r][c]
        
        return rotatedBox


        