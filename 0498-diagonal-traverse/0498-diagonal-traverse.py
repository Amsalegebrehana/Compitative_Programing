class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = defaultdict(list)
        M, N = len(mat), len(mat[0])
        r = set()
        for i in range(M):
            for j in range(N):
                if (i,j) not in r:
                    
                    ans[i+j].append(mat[i][j])

        result = []
        for i in ans:
            if i % 2 == 0:
                result.extend(ans[i][::-1])
            else:
                result.extend(ans[i])
        return result
        