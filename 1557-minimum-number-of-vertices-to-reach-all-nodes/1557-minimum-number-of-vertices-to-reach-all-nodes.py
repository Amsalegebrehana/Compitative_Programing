class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = defaultdict(int)
        ans = []
        for i , j in edges:
            incoming[j] += 1

        for i in range(n):
            if incoming[i] == 0:
                ans.append(i)
        return ans