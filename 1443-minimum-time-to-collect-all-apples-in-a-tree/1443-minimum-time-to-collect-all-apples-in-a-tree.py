class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(set)
        visited = set()
        res = 0
        queue = deque()
        for i,j in edges:
            if j in graph.keys(): 
                graph[i].add(j)
            graph[j].add(i)
        for i in range(n):
            if  hasApple[i]:
                # visited.add(i)
                queue.append(i)
            
        while queue:
            curr = queue.popleft()
            hasApple[curr] = True
            visited.add(curr)

            for nebour in graph[curr]:
               
                if nebour not in visited:
                   
                    queue.append(nebour)
        for i in range(1,n):
            if hasApple[i]:
                res+=2
        return res
            
                