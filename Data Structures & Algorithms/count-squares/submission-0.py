class CountSquares:

    def __init__(self):
        self.points_cnt = defaultdict(int)
        self.points = set()
        

    def add(self, point: List[int]) -> None:
        self.points_cnt[tuple(point)] += 1
        self.points.add(tuple(point))
        
    def count(self, point: List[int]) -> int:
        px,py = point
        result = 0
        point_count = self.points_cnt[(px,py)] if self.points_cnt[(px,py)] > 0 else 1
        for x,y in self.points:
            if abs(px-x) == abs(py - y) and (x,y) != (px,py):         
                if (px,y) in self.points and (x, py) in self.points:
                    result += (
                               self.points_cnt[(px,y)] * self.points_cnt[(x, py)] *
                               self.points_cnt[(x,y)] *  point_count
                            )
        
        return result
        
