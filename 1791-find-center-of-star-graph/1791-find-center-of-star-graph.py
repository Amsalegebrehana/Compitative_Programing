class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(int)
        for i,j in edges:
        
            graph[i]+=1
            graph[j]+=1
        
        maxval, star = 0, 0
        for key, val in graph.items():
            if val > maxval:
                maxval = val
                star = key
        return star
            