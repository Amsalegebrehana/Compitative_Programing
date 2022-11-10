class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        result = []
        def backtrack(start, cur_val, path):
            if cur_val == 0:
                result.append(list(path))
                return 
            if cur_val <0:
                return
            for j in range(start,size):
                path.append(candidates[j])
                backtrack(j, cur_val - candidates[j], path)
                path.pop()
        backtrack(0, target, [])
        return result