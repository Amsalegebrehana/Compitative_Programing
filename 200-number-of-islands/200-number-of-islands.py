class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        noIslands = 0
        dir_arr = [[0,1], [0,-1],[1,0], [-1,0]]
      
        def bound(r,c):
            if 0<= r < len(grid) and 0<= c < len(grid[0]):
                return True
            return False
        def bfs(r,c):
            queue = deque([[r,c]])
            while queue:
                curr = queue.popleft()
                for i, j in dir_arr:
                    nr, nc = curr[0] + i, curr[1] + j
                    if bound(nr,nc) and grid[nr][nc] == '1':
                       
                        grid[nr][nc] = '2'
                        queue.append([nr,nc])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i,j)
                    noIslands +=1
                
      
        return noIslands
                       
                        
            