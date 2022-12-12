class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dir_arr = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque([(sr,sc)])
        visited = {(sr,sc)}
        
        start = image[sr][sc]
        image[sr][sc] = color
        
        def bound(r,c):
            return len(image) > r >= 0 and len(image[0]) > c >= 0
        while queue:
            curr = queue.popleft()
            for r,c in dir_arr:
                nr,nc = r + curr[0], c + curr[1]
                if bound(nr,nc) and image[nr][nc] == start and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc))
                    image[nr][nc] = color
        return image