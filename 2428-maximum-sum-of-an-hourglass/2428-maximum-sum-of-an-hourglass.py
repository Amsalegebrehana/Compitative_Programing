class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxsum = 0
        M = len(grid)
        N = len(grid[0])
                
        for i in range(1, M - 1):
            for j in range(1, N - 1):
                currsum = grid[i][j] +grid[i-1][j] + grid[i-1][j-1] + grid[i-1][j+1] + grid[i+1][j] + grid[i+1][j - 1] +grid[i+1][j+ 1]
                maxsum = max(maxsum, currsum)
        return maxsum