class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        size = len(nums)
        def backtrack(start, path):
            result.append(list(path))
            for j in range(start, size):
                if j >  start and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                backtrack(j+1, path)
                path.pop()
        backtrack(0,[])
        return result
            