class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
            dir_arr = [(1,0),(0,1),(-1,0),(0,-1)]
            M = len(board)
            N = len(board[0])
            def bound(r,c):
                return M > r >= 0 and N > c >= 0
            def backtrack(pathword, r,c):
                if "".join(pathword) == word:
                    return True

                for i, j  in dir_arr:
                   
                    newr, newc = r + i, c + j
                    if bound(newr,newc) and board[newr][newc] == word[len(pathword)]:
                        pathword.append(board[newr][newc])
                        board[newr][newc] = "#"
                        if backtrack(pathword, newr,newc):
                            return True
                        
                        board[newr][newc] = pathword.pop()
                return False
            for r in range(M):
                for c in range(N):
                    if board[r][c] == word[0]:
                        pathword = [board[r][c]]
                        board[r][c] = "#"
                        if backtrack(pathword,r,c):
                            return True
                        board[r][c] = pathword.pop()
            return False
            