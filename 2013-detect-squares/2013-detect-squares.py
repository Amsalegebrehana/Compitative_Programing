class DetectSquares:

    def __init__(self):
        
        self.points = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
    
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0 
        px,py = point
        for x,y in self.points.keys():
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            if (x,py) in self.points and (px,y) in self.points:
                res += self.points[(x,py)] * self.points[(px,y)] * self.points[(x,y)]
        
        return res   

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)