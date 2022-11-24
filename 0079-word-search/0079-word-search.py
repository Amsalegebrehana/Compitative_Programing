class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir_arr = [(0,-1),(-1,0),(1,0),(0,1)]
        strings = set()
        visited = set()
        M,N =  len(board), len(board[0])
        def bound(r,c):
            return  M > r >= 0 and N > c >= 0
              
        def backtrack(start,i):
            if i == len(word) :
                return True
            val = False
            for r,c in dir_arr:
                nr,nc = r + start[0], c + start[1]
                if bound(nr,nc) and (nr,nc) not in visited and board[nr][nc] == word[i]:
                    visited.add((nr,nc))
                    val =  backtrack((nr,nc), i + 1)
                    if val:
                        return True
                    visited.remove((nr,nc))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    var = backtrack((i,j), 1)
                    if var:
                        return True
                    visited.remove((i,j))
              
               
        return False