class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        incoming = defaultdict(int)
        result = defaultdict(set)
        graph = defaultdict(set)
        for i , j in edges:
            incoming[j] +=1
            graph[i].add(j)
        queue = deque([])
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)
                
                
        while queue:
            curr = queue.popleft()
            for next_node in graph[curr]:
                incoming[next_node] -=1
                result[next_node] = result[next_node] | result[curr]
                result[next_node].add(curr)
                if incoming[next_node] == 0:
                        queue.append(next_node)
        answer = []
        for i in range(n):
            temp = sorted(list(result[i]))
            answer.append(temp)
        return answer
        