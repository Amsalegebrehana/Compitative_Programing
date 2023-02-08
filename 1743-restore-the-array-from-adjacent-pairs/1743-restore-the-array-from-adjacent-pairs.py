class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        nebours = defaultdict(int)
        visited = set()
        result = []
        queue = deque([])
        for i , j in adjacentPairs:
            graph[i].add(j)
            graph[j].add(i)
            nebours[i] +=1
            nebours[j] +=1

        for num in nebours:
            if nebours[num] == 1:
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
        