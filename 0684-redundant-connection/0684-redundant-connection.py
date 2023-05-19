class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        size = len(edges)
        parent = [i for i in range(size)]
        rank = [1] * size
        ans = []
        
        def find(a):
            if a == parent[a]:
                return a
            parent[a] = find(parent[a])
            return parent[a]
        
        def union(a,b):
            pa = find(a)
            pb = find(b)
            
            if pa == pb:
                ans.append([a+1,b+1])
                
            elif rank[pa] > rank[pb]:
                parent[pb] = pa
            elif rank[pa] < rank[pb]:
                parent[pa] = pb
            else:
                parent[pb] = pa
                rank[pa] +=1
                
        for i, j in edges:
            union(i-1,j-1)

        return ans[-1]