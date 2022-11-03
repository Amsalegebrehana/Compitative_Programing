class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        matrix = [[False for i in range(numCourses)] for j in range(numCourses)]
        for i,j in prerequisites:
            matrix[i][j] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
        return [matrix[i][j] for i, j in queries]