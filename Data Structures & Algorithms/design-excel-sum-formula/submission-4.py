from collections import defaultdict

class Excel:

    def __init__(self, height: int, width: str):
        self.H = height
        self.W = ord(width) - ord('A') + 1
        self.excel = [[0]*self.W for i in range(self.H)]
        self.dependents = defaultdict(set)
        self.formulas = {}

    def _col(self, column):
        return ord(column) - ord('A') 
    
    def _recalculate(self, row, column):
        total = 0
        for (dr, dc), count in self.formulas[(row, column)].items():
            total += self.excel[dr][dc]*count
        
        self.excel[row][column] = total
    
    def _update_dependents(self,row,column):
        for r,c in self.dependents[(row,column)]:
            self._recalculate(r,c)
            self._update_dependents(r,c)

    def set(self, row: int, column: str, val: int) -> None:
        r = row - 1
        c = self._col(column)

        if (r,c) in self.formulas:
            for (dr,dc) in self.formulas[(r,c)]:
                self.dependents[(dr,dc)].discard((r,c)) # Discard in set to remove the element 
            
            self.formulas.pop((r,c))
        
        self.excel[r][c] = val
        self._update_dependents(r,c)
        

    def get(self, row: int, column: str) -> int:
        col = self._col(column)
        return self.excel[row-1][col]

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        res = 0
        col = self._col(column)
        row = row - 1

        counter = defaultdict(int)
        
        for number in numbers:
            if ':' not in number:
                rr = int(number[1:]) - 1
                cc = self._col(number[0])
                counter[(rr,cc)] += 1
                self.dependents[(rr,cc)].add((row,col))
            else:
                start, end = number.split(':')
                row1, col1 = int(start[1:]) - 1 , ord(start[0]) - ord('A')
                row2, col2 = int(end[1:]) - 1, ord(end[0]) - ord('A')

                for r in range(row1, row2 + 1):
                    for c in range(col1, col2 + 1):
                        counter[(r,c)] += 1
                        self.dependents[(r,c)].add((row,col))

        if (row,col) in self.formulas:
            for (dr,dc) in self.formulas[(row,col)]:
                self.dependents[(dr,dc)].discard((row,col)) # Discard in set to remove the element 

        self.formulas[(row,col)] = counter
        self._recalculate(row,col)
        self._update_dependents(row,col)

        return self.get(row+1,column)

    # def calculate_number_sum(self,number):
    #     row = number[1] - 1
    #     col = ord(number[0]) - ord('A')
    #     return self.excel[row][col]


        


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
