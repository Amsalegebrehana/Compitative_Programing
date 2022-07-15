class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # print(board)
        rook = []
        result = 0
        dir_arr = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook= [i,j]
        visited = set()
        i,j = rook[0],rook[1]
     
          
        for r, c in dir_arr:
            nr= i+r
            nc=j+c
            while 8 > nr >= 0 and 8 >nc>= 0 and board[nr][nc] != 'B':
                if board[nr][nc] != '.':

                    if board[nr][nc] == 'p' :
                        result += 1
                        
                    break
                nr +=r
                nc +=c
        
        return result