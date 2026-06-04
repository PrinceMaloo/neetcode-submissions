class CountSquares:

    def __init__(self):
        self.points_cnt = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points_cnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px,py = point
        result = 0
        # point_count = self.points_cnt[(px,py)] if self.points_cnt[(px,py)] > 0 else 1
        for x,y in self.points_cnt:
            if abs(px-x) == abs(py - y) and (x,y) != (px,py):         
                    result += (
                               self.points_cnt.get((px,y), 0) * self.points_cnt.get((x, py),0) *
                               self.points_cnt[(x,y)]
                            )
        
        return result
        
