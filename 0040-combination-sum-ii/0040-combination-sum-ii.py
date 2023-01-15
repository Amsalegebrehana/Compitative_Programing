class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        size = len(candidates)
        result = []
        sett = set()
        def backtrack(start, val, path):
            if val == 0:
              
                result.append(list(path))
                return
            
          
            for i in range(start, size):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if val - candidates[i] < 0:
                    break
                path.append(candidates[i])
                backtrack(i+1, val - candidates[i], path)
                path.pop()
       
        backtrack(0,target,[])
        return result