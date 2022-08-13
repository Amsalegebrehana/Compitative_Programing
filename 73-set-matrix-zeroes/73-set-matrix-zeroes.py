class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rset = set()
        cset = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rset.add(i)
                    cset.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rset or j in cset:
                   
                    matrix[i][j] = 0