class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = defaultdict(list)
       
        result = []
        for i, j in edges:
            indegree[j].append(i)
       
        for i in range(n):
            if i not in indegree:
                result.append(i)
        return result