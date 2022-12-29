class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ts = set(target)
        op = []
        for i in range(1, n+1):
            if i > target[-1]:
                break
            if i in ts:
                op.append("Push")
            else:
                op.append("Push")
                op.append("Pop")
        return op