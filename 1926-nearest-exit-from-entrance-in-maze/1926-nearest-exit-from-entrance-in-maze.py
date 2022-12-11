class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        dir_arr = [(1,0),(0,1),(-1,0),(0,-1)]
        dist = inf
        queue = deque([(entrance[0], entrance[1],0)])
        visited = {(entrance[0], entrance[1])}
        M = len(maze)
        N = len(maze[0])
        def bound(r, c):
            return M > r >= 0 and N > c >= 0
        while queue:
            curr = queue.popleft()
            for r, c in dir_arr:
                nr, nc = r + curr[0], c + curr[1]
                if bound(nr,nc) and maze[nr][nc] == "." and (nr,nc) not in visited:
                 
                    if nr == M - 1 or nc == N - 1 or nr == 0 or nc == 0:
                        
                        dist = min(dist, curr[2] + 1)
                    queue.append(((nr,nc, curr[2] + 1)))
                    visited.add((nr,nc))
  
        return dist if dist != inf else -1