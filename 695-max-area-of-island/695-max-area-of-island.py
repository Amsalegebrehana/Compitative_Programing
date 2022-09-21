class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        dir_arr = [[0,1],[1,0],[0,-1],[-1,0]]
        def bound(r,c):
            if 0<= r < len(grid) and 0<= c < len(grid[0]):
                return True
            return False
        def bfs(r,c):
            queue = deque([[r,c]])
            visited.add((r,c)) 
            c = 1
            while queue:
                curr = queue.popleft()
               
                for i, j in dir_arr:
                    nr,nc = curr[0] + i, curr[1] + j
                    if bound(nr,nc) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append([nr,nc])
                        c+=1
            return c
                        
        maxcount = 0

        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                if grid[i][j] == 1 :
               
                    maxcount = max(maxcount, bfs(i,j))
        return maxcount

            
            
        