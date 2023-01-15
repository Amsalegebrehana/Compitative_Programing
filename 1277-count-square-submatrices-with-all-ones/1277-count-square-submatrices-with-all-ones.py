class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        result = 0
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                result += matrix[i][j] 
        return result
        