class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        ans = [ [mat[r][c] for c in range(N)] for r in range(M)]
       
        for i in range(M):
            for j in range(1, N):
                ans[i][j] += ans[i][j - 1]
                
        for i in range(1, M):
            for j in range( N):
                ans[i][j] += ans[i - 1][j]

        
        for i in range(M):
            for j in range( N):
                r, c  = max(0, i - k), max(0, j- k)
                r2 , c2 = min(M - 1, i + k), min(N-1, j + k)
                f= ans[r - 1][c2] if r > 0 else 0
                s = ans[r2][c - 1] if c > 0 else 0
                t = ans[r - 1][c - 1] if r > 0 and c > 0 else 0
                mat[i][j] = ans[r2][c2] - f - s + t
        return mat