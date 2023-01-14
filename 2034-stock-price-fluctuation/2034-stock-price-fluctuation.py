class StockPrice:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.highesttime = 0
        self.stock = {}
    def update(self, timestamp: int, price: int) -> None:
        self.highesttime = max(self.highesttime,timestamp)
     
        self.stock[timestamp] = price
       
        heappush(self.maxheap, (-price, timestamp))
        heappush(self.minheap, (price, timestamp))
    def current(self) -> int:
        
        return  self.stock[self.highesttime]
    
    def maximum(self) -> int:
       
        maxval, currtime =  heappop(self.maxheap)
        while -maxval != self.stock[currtime]:
            maxval, currtime  = heappop(self.maxheap)
        heappush(self.maxheap, (maxval, currtime))
        return -maxval

    def minimum(self) -> int:
    
        minval, currtime =  heappop(self.minheap)
        while minval != self.stock[currtime]:
            minval, currtime  = heappop(self.minheap)
        heappush(self.minheap, (minval, currtime))
        return minval


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()