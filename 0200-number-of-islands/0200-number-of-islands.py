class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIsland= 0
        N= len(grid[0])
        M = len(grid)
        def bound(r,c):
            return M > r >= 0 and N> c>= 0
        def bfs(r,c):
            queue = deque([(r, c)])
            dir_arr = [(0,1),(1,0),(-1,0),(0,-1)]
            while queue:
                curr = queue.popleft()
                for i, j in dir_arr:
                    nr , nc = curr[0] + i, curr[1] + j
                    if bound(nr,nc) and grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        grid[nr][nc] = "2"
        for r in range(M):
            for c in range(N):
                if grid[r][c] == "1":
                    bfs(r,c)
                    numIsland+=1
        return numIsland
