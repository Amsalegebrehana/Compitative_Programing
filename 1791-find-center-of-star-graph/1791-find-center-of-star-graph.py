class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(set)

        for i,j in edges:
        
            graph[i].add(j)
            graph[j].add(i)
        
        maxval = 0
        star = 0

        for key, val in graph.items():
            if len(val) > maxval:
                maxval = len(val)
                star = key

      
        return star
            