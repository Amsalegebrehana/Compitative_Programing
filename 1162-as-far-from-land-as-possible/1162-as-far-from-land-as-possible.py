class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        dist = 0
        dir_arr = [(1,0),(0,1), (-1,0),(0,-1)]
        queue = deque([])
        M = len(grid)
        visited = set()
        for r in range(M):
            for c in range(M):
                if grid[r][c] == 1:
                    queue.append((r,c))
                    visited.add((r,c))

        def bound(r,c):
            return M > r >=0 and M > c >= 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
     
                for r,c in dir_arr:
                    nr,nc = r + curr[0], c + curr[1]
                    if bound(nr,nc) and grid[nr][nc] == 0 and (nr,nc) not in visited:
                        
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                        
            if queue:
                dist +=1
        return dist if dist != 0 else -1
        