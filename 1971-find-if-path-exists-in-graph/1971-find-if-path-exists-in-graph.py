class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        queue = deque([source])
        visited = set([source])
   
        while queue:
            curr = queue.popleft()
            if curr == destination:
                return True
            for i in adj[curr]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        return False
                