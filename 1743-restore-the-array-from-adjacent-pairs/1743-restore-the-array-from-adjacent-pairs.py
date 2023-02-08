class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        visited = set()
        result = []
        queue = deque([])
        
        for i , j in adjacentPairs:
            graph[i].add(j)
            graph[j].add(i)

        for num in graph:
            if len(graph[num] )== 1:
                start = num
                visited.add(num)
                
                break
  
        result.append(start)
        queue.append(start)
        while queue:
            curr = queue.popleft()
            for n in graph[curr]:
                if n not in visited:
                    result.append(n)
                    queue.append(n)
                    visited.add(n)
        return result
        