class RandomizedCollection:

    def __init__(self):
        self.number_indx = defaultdict(set)
        self.numbers = []

    def insert(self, val: int) -> bool:
        self.numbers.append(val)
        size = len(self.numbers)
        self.number_indx[val].add(size - 1)
        if  len(self.number_indx[val]) == 1:
            
            return True
        return False
            
      
    def remove(self, val: int) -> bool:
        size = len(self.numbers)
        if len(self.number_indx[val]) >= 1:
            curr_idx = self.number_indx[val].pop()
            self.number_indx[self.numbers[-1]].add(curr_idx)
            self.number_indx[self.numbers[-1]].remove(size - 1)
            self.numbers[curr_idx], self.numbers[-1] = self.numbers[-1], self.numbers[curr_idx]
            self.numbers.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.numbers)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()