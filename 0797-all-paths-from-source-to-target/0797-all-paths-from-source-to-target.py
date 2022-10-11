class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        def btrack(node, path):
            path.append(node)
            if node == len(graph) -1:
                
                self.res.append(path[:])
            for n in graph[node]:
                btrack(n, path)
            path.pop()
        btrack(0, [])
        return self.res
        