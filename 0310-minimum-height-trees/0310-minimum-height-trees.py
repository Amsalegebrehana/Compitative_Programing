class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegrees = defaultdict(int)
        if n == 1:
            return [0]
        for i , j in edges:
            graph[i].add(j)
            graph[j].add(i)
            indegrees[j] +=1
            indegrees[i] +=1
       
        source = deque()
        for i in range(n):
            if indegrees[i] == 1:
                source.append(i)
     
        res = []
        while source:
            size = len(source)
            temp = []
            for i in range(size):
                curr = source.popleft()
                temp.append(curr)
                for node in graph[curr]:
                    indegrees[node] -=1
                    if indegrees[node] == 1:
                      
                        source.append(node)
            if not source:
                res = temp
        return res
                    