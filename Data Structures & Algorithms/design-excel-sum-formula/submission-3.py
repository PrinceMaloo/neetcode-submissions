from collections import defaultdict
from typing import List

class Excel:

    def __init__(self, height: int, width: str):
        self.H = height
        self.W = ord(width) - ord('A') + 1
        self.values = [[0] * self.W for _ in range(height)]
        
        self.formulas = {}  # (r,c) -> { (r,c): count }
        self.dependents = defaultdict(set)  # reverse graph

    def _col(self, c):
        return ord(c) - ord('A')

    def set(self, row: int, column: str, val: int) -> None:
        r, c = row - 1, self._col(column)

        # Remove old formula if exists
        if (r, c) in self.formulas:
            for (dr, dc) in self.formulas[(r, c)]:
                self.dependents[(dr, dc)].discard((r, c))
            del self.formulas[(r, c)]

        self.values[r][c] = val
        self._update_dependents(r, c)

    def get(self, row: int, column: str) -> int:
        return self.values[row-1][self._col(column)]

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        r, c = row - 1, self._col(column)

        counter = defaultdict(int)

        for num in numbers:
            if ':' not in num:
                rr = int(num[1:]) - 1
                cc = self._col(num[0])
                counter[(rr, cc)] += 1
            else:
                start, end = num.split(':')
                r1, c1 = int(start[1:]) - 1, self._col(start[0])
                r2, c2 = int(end[1:]) - 1, self._col(end[0])

                for i in range(r1, r2 + 1):
                    for j in range(c1, c2 + 1):
                        counter[(i, j)] += 1

        # Remove old formula
        if (r, c) in self.formulas:
            for dep in self.formulas[(r, c)]:
                self.dependents[dep].discard((r, c))

        self.formulas[(r, c)] = counter

        for dep in counter:
            self.dependents[dep].add((r, c))

        self._recalculate(r, c)
        self._update_dependents(r, c)

        return self.values[r][c]

    def _recalculate(self, r, c):
        total = 0
        for (rr, cc), count in self.formulas[(r, c)].items():
            total += self.values[rr][cc] * count
        self.values[r][c] = total

    def _update_dependents(self, r, c):
        for dr, dc in self.dependents[(r, c)]:
            self._recalculate(dr, dc)
            self._update_dependents(dr, dc)