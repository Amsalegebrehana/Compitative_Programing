class MapSum:

    def __init__(self):
        self.pair = defaultdict(int)
        self.vis = defaultdict(int)
    def insert(self, key: str, val: int) -> None:
        for i in range(len(key)):
            if key in self.vis:
                self.pair[key[:i+1]] += val  - self.vis[key]
            else:
                self.pair[key[:i+1]] += val

        self.vis[key] = val

    def sum(self, prefix: str) -> int:

        return self.pair[prefix]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)