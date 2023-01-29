class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        res = []
        order = []
        M, N = len(score), len(score[0])
        for i in range(M):
            order.append((score[i][k], i))
        order.sort()

        for i in range(len(order)-1,-1,-1):
            res.append(score[order[i][1]])
        return res