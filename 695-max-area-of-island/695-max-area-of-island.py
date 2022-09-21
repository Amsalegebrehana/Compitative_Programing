class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        dir_arr = [[0,1],[1,0],[0,-1],[-1,0]]
        def bound(r,c):
            if 0<= r < len(grid) and 0<= c < len(grid[0]):
                return True
            return False
        def dfs(r,c):
            visited.add((r,c)) 
            ct = 1  
            for i, j in dir_arr:
                nr,nc = r + i, c + j
                if bound(nr,nc) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    ct += dfs(nr,nc)
            return ct
                        
        maxcount = 0

        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited :
                    maxcount = max(maxcount, dfs(i,j))
        return maxcount

            
            
        