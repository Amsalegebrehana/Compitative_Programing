class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        dir_arr = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = deque([(0,0)])
        M = len(heights[0])
        
        N = len(heights)
        efforts = [[inf  for _ in range(M)] for _ in range(N)]

        efforts[0][0] = 0
        def bound(r,c):
            if 0<= r < len(heights) and 0<= c < len(heights[0]):
                return True

        visited = set()
        while queue:
   
            r,c = queue.popleft()
            curr = heights[r][c]
            for i, j in dir_arr:
                nr,nc = r + i, c + j
                if bound(nr,nc) :
                    effort = max(efforts[r][c],abs(heights[nr][nc] - curr))
                    
                    if effort < efforts[nr][nc]:
                        efforts[nr][nc] = effort
                        queue.append((nr,nc))
      
        
        return efforts[N-1][M-1]