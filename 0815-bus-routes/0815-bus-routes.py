class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(set)
        
        for i in range(len(routes)):
            for j in routes[i]:
                graph[j].add(i)
                
        targets = [(source, 0)]
        visited = set([source])
        
        for stop, bus in targets:
            if stop == target: 
                return bus
            for i in graph[stop]:
                for j in routes[i]:
                    if j not in visited:
                        targets.append((j, bus + 1))
                        visited.add(j)
                routes[i] = []  
        return -1
        