class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        result = []
        def backtrack(start, path):
            result.append(list(path))
            for j in range(start, size):
                path.append(nums[j])
                backtrack(j+1, path)
                path.pop()
        backtrack(0,[])
        return result