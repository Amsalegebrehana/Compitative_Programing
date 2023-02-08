class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1],values[i]))
            graph[equations[i][1]].append((equations[i][0],1/values[i]))       

        result = [] 
        def bfs(a,b):
          
            if a not in graph:
                return -1.0
            
            queue = deque([(a,1)])
            visited = set()
            
            while queue:
                curr, val = queue.popleft()
                if curr == b :
                    return val
                if curr not in graph:
                    return -1.0
                for ne in graph[curr]:
                    if ne[0] not in visited:
                        queue.append((ne[0], val * ne[1]))
                        visited.add(ne[0])
            return -1 
        for a, b in queries:
            result.append(bfs(a,b))
        return result
            
            
        