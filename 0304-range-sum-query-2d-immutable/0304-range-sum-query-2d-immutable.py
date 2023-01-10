class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        M,N = len(matrix),len(matrix[0])
        self.prefsum = [[0 for _ in range(N)] for _ in range(M)]
     
        self.prefsum[0][0] = matrix[0][0]
        for i in range(1, N):
            self.prefsum[0][i] =  self.prefsum[0][i-1]  + matrix[0][i]
        for i in range(1,M):
             self.prefsum[i][0]  =  self.prefsum[i - 1][0] + matrix[i][0]
    
        for r in range(1,M):
            for c in range(1,N):
                
                self.prefsum[r][c] = self.prefsum[r-1][c] + self.prefsum[r][c-1] -  self.prefsum[r-1][c-1] + matrix[r][c]
    
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r2col = self.prefsum[row2][col1-1] if col1 else 0
        r1col = self.prefsum[row1-1][col2] if row1 else 0
        b = self.prefsum[row1-1][col1-1] if col1 and row1 else 0
        return self.prefsum[row2][col2] - r2col- r1col +  b


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)