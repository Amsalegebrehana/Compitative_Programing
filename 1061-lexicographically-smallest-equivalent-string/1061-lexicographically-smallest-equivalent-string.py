class UnionFind:
    def __init__(self):
        self.parent = [i for i in range(26)]
        
    def find(self, x):
        
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
            
        return x
    
    def union(self, x, y):
        
        px = self.find(x)
        py = self.find(y)
        
        if px != py:
            px,py = sorted([px,py])
            self.parent[py] = self.parent[px]
        
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        val_a = ord("a")
        unionfind = UnionFind()
        minorders = []
        for i in range(len(s1)):
            unionfind.union(ord(s1[i])- val_a, ord(s2[i])- val_a)
            
        for i in range(len(baseStr)):
            num_val_i = ord(baseStr[i]) - val_a
            smallest = chr(val_a + (unionfind.find(num_val_i)))
            minorders.append(smallest)

        return "".join(minorders)
        
        
            
            
            
            
            
            
            
        