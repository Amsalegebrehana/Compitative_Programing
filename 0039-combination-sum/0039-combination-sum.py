class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
 
        result = []
        def backtrack(start, val, path):
            if val == 0:
                result.append(list(path))
                return
            if val < 0:
                return 
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, val - candidates[i], path)
                path.pop()
        backtrack(0, target, [])
        return result
                