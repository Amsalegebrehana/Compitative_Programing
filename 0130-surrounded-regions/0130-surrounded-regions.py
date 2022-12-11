class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])
        queue = deque([])
        visited = set()
        dir_arr = [(1,0),(0,1),(-1,0),(0,-1)]

        for i in range(M):
            if board[i][0] == "O":
                queue.append((i,0))
                visited.add((i,0))
        for i in range(M):
            if board[i][N-1] == "O":
                queue.append((i,N-1))
                visited.add((i,N-1))
        for i in range(N):
            if board[0][i] == "O":
                queue.append((0,i))
                visited.add((0,i))
        for i in range(N):
            if board[M-1][i] == "O":
                queue.append((M- 1, i))
                visited.add((M-1, i))

        def bound(r,c):
            return M > r >= 0 and N > c >= 0
        while queue:
            curr = queue.popleft()
            for r, c in dir_arr:
                nr,nc = r + curr[0], c + curr[1]
                if bound(nr,nc) and  board[nr][nc] == "O" and (nr,nc) not in visited:
                    queue.append((nr,nc))
                    visited.add((nr,nc))

        for r in range(M):
            for c in range(N):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"
                    visited.add((r,c))
                    