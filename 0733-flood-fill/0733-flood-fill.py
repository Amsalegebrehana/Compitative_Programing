class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dir_arr  = [(1,0),(0,1),(-1,0),(0,-1)]
        org = image[sr][sc]
        image[sr][sc] = color
        queue = deque([(sr,sc)])
        visited = set((sr,sc))
        M = len(image)
        N = len(image[0])
        def bound(r,c):
            return M > r>= 0 and N > c >= 0
        while queue:
            row,col = queue.popleft()
            for r, c in dir_arr:
                newrow, newcol = row + r, col + c
                if bound(newrow,newcol) and image[newrow][newcol] == org and (newrow, newcol) not in visited:
                    
                    image[newrow][newcol] = color
                    
                    queue.append((newrow, newcol))
                    visited.add((newrow, newcol))
        return image