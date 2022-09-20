class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
       
        visited = set()
        dir_arr = [[0,1], [0,-1],[1,0], [-1,0]]
        def bound(r,c):
            if 0<= r < len(grid) and 0<= c < len(grid[0]):
                return True
            return False
        for i in range(0, len(grid[0])):
            if grid[0][i] == 'O':
                visited.add((0,i))
        for i in range(0, len(grid)):
            if grid[i][0] == 'O':
                visited.add((i,0))
    
                
        for i in range(0, len(grid[0])):
           
            if grid[len(grid) - 1][i] == 'O':
                visited.add((len(grid) - 1,i)) #bottom
        for i in range(0, len(grid)):
            
          
            if grid[i][len(grid[0]) - 1] == 'O':
                visited.add((i,len(grid[0]) - 1))
        def bfs(r,c):
            queue = deque([(r,c)])
            while queue:
                curr = queue.popleft()
                if curr in visited:
                    for i , j in dir_arr:
                        nr,nc = curr[0] + i, curr[1] + j
                        if bound(nr,nc) and (nr,nc) not in visited and grid[nr][nc] == "O":
                            visited.add((nr,nc))
                            queue.append((nr,nc))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                bfs(i,j)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "O":
                    grid[i][j] = 'X'
                    
                
            
                
            
                
        