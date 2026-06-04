class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        start = 0
        end = n - 1
        while(start < end):
            for i in range(n-1):
                for index in range(end, start, -1):
                    matrix[start][index], matrix[start][index - 1] = matrix[start][index-1], matrix[start][index]

                for index in range(start, end, 1):
                    matrix[end][index], matrix[end][index + 1] = matrix[end][index+1], matrix[end][index]
                
                matrix[start][start], matrix[end][end] =  matrix[end][end], matrix[start][start]

                for index in range(start, end-1, 1):
                    matrix[index][start], matrix[index + 1][start] = matrix[index + 1][start], matrix[index][start]

                for index in range(end, start + 1, -1):
                    matrix[index][end], matrix[index - 1][end] = matrix[index - 1][end], matrix[index][end]
                

            start += 1
            end -= 1
            n -= 2

            

    



        
        