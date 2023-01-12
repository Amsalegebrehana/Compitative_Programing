class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, path):
         
            result.append(list(path))
            for j in range(start, len(nums)):
                path.append(nums[j])
      
                backtrack(j+1, path)
                path.pop()
        backtrack(0,[])
        return result