class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        M,N = len(mat), len(mat[0])
        dir_arr = [(0,1),(1,0),(0,-1),(-1,0)]
        queue= deque([])
        visited = set()
       
  
        dist = 0
        for r in range(M):
            for c in range(N):
                if mat[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
                    
        def bound(r,c):
            return M > r >= 0 and N > c >= 0
        
        while queue:
            size = len(queue)
            dist +=1
            for _ in range(size):
                r,c = queue.popleft()
                for i, j in dir_arr:
                    newr, newc = r + i, c + j
                    if bound(newr,newc) and (newr,newc) not in visited:
                        mat[newr][newc] = dist
                        visited.add((newr,newc))
                        queue.append((newr,newc))
        return mat
                
        