class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colorArray = [-1] * len(graph)
        queue = deque()
        for i in range(len(graph)):
            if colorArray[i] == -1:
                colorArray[i] = 1
                queue.append(i)
            while queue:
                curr = queue.popleft()
                for nebours in graph[curr]:
                    if colorArray[nebours] == -1:
                        
                        colorArray[nebours] = 0 if colorArray[curr] == 1 else 1
                        queue.append(nebours)
                    elif colorArray[nebours] == colorArray[curr]:
                        return False
        return True