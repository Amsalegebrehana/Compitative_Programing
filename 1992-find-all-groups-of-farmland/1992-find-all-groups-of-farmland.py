class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        visited = set()
        dir_arr =  dir_arr = [[1,0],[0,1],[0,-1],[-1,0]]
        def bound(r,c):
            if 0<= r < len(land) and 0<= c < len(land[0]):
                return True
            return False
        
        def bfs(r,c):
            temp = [[r,c]]
            queue = deque([[r,c]])
            visited.add((r,c))
            while queue:
                curr = queue.popleft()
                for i, j in dir_arr:
                    nr, nc = curr[0] + i, curr[1] + j
                    if bound(nr,nc) and land[nr][nc] == 1 and (nr,nc) not in visited:
                        queue.append([nr,nc])
                        visited.add((nr,nc))
                        temp.append([nr,nc])
            l = temp[0]
            l.extend(temp[-1])
            return l
        ans = []
        for i in range(len(land)):
            
            for j in range(len(land[0])):
                if land[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    ans.append(bfs(i,j))
                  
        return ans
                    
                        
                