class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        noIslands = 0
        dir_arr = [[0,1], [0,-1],[1,0], [-1,0]]
      
        def bound(r,c):
            if 0<= r < len(grid) and 0<= c < len(grid[0]):
                return True
            return False
        def dfs(r,c):
            
            for i, j in dir_arr:
                nr, nc = r + i, c + j
                if bound(nr,nc) and grid[nr][nc] == '1':

                    grid[nr][nc] = '2'
                    dfs(nr,nc)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    noIslands +=1
                
      
        return noIslands
                       
                        
            