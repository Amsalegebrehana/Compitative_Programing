class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        dir_arr = [[1,0],[0,1],[0,-1],[-1,0]]
       
        def bound(r,c):
            if 0<= r < len(grid) and 0<= c < len(grid[0]):
                return True
            return False
        def bfs(r,c):
            queue = deque([[r,c]])
            p = 0
            visited.add((r,c))
            while queue:
                curr = queue.popleft()
                for i, j in dir_arr:
                    nr,nc = curr[0] + i, curr[1] + j 
                    if not bound(nr,nc) or  bound(nr,nc) and grid[nr][nc] == 0:
                        p += 1
                    if bound(nr,nc) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append([nr,nc])
            return p
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    return bfs(i,j)