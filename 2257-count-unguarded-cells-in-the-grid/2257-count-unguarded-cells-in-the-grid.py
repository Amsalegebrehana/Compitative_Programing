class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        newgrid  = []
        result = 0
        for i in range(m):
            newgrid.append([0]*n)
       
        for i,j in guards:
            newgrid[i][j] = 1
        for i, j in walls:
            newgrid[i][j] = 1
      
        dir_arr = [[1,0],[0,1],[-1,0],[0,-1]]
        for i,j in guards:
            for r,c in dir_arr:
                nr = i + r
                nc = j + c
                while m > nr >=0 and n > nc >= 0 and (newgrid[nr][nc] == 0 or newgrid[nr][nc] == 2):
                    newgrid[nr][nc] = 2
                    nr +=r
                    nc += c
       
        for i in range(m):
            for j in range(n):
                if newgrid[i][j] == 0:
                    result +=1
        return result
                
            