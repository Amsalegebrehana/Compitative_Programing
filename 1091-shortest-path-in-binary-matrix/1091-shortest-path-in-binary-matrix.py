class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        if len(grid) == 1 and grid[0][0] == 0:
            return 1
        M,N = len(grid), len(grid[0])
        dir_arr = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        queue= deque([(0,0)])
        visited = {(0,0)}
        path = 0
                      
        def bound(r,c):
            return M > r >= 0 and N > c >= 0
        
        while queue:
            size = len(queue)
            path += 1
            
            for _ in range(size):
                r,c = queue.popleft()
                for i,j in dir_arr:
                    new_r, new_c = r + i , j + c
                    if bound(new_r , new_c) and (new_r , new_c) not in visited and grid[new_r][new_c] == 0:
                        if (new_r , new_c) == (M-1, N-1):
                            return path + 1
                        queue.append((new_r , new_c))
                        visited.add((new_r , new_c))
        return -1