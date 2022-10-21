class RandomizedSet:

    def __init__(self):
        self.store = defaultdict()
        self.numbers = []

    def insert(self, val: int) -> bool:
        size = len(self.numbers)
        if val in self.store:
            return False
        else:
            self.store[val] = size 
            self.numbers.append(val)
            return True
        
    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False
       
        cur_idx = self.store[val]
        self.store[ self.numbers[-1]] = cur_idx
        self.numbers[cur_idx], self.numbers[-1] =  self.numbers[-1],  self.numbers[cur_idx]
        self.numbers.pop()
        del self.store[val]
        return True

    def getRandom(self) -> int:

        return random.choice(self.numbers)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()