class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        dir_arr = [(1,0), (0, 1), (-1,0), (0,-1)]
        queue = deque([])
        visited = set()
        M = len(grid)
        N = len(grid[0])
        
        def bound(r,c):
            return M > r >= 0 and N > c >= 0
       
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 2 and (r,c) not in visited:
                    visited.add((r,c))
                    queue.append((r,c,0))
        while queue:
           
            curr = queue.popleft()
            for r,c in dir_arr:
                nr,nc = curr[0] + r, curr[1] + c
                if bound(nr, nc) and  grid[nr][nc] == 1 and (nr,nc) not in visited:
                    minutes = curr[2] + 1
                    queue.append((nr,nc, minutes))
                    visited.add((nr,nc))
                    grid[nr][nc] = 2
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    return -1
        return minutes
            
                        
                
        
        