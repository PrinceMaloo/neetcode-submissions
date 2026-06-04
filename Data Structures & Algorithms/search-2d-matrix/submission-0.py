class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = (rows*cols)-1

        for i in range(rows):
            for j in range(cols):
                array.append(matrix[i][j])
            
        while(left<= right):
            mid = (left + right)//2
            if(array[mid] > target):
                right = mid - 1
            elif(array[mid] < target):
                left = mid + 1
            else:
                return True
        
        return False

            
            
        


        

       

        