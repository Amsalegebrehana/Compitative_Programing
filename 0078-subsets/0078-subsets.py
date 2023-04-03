class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(current_arr, start):
            
            if start >= len(current_arr):
                res.append(list(current_arr))
                
                
            for i in range(start, len(nums)):
                
                current_arr.append(nums[i])
                backtrack(current_arr, i+1)
                current_arr.pop()
        backtrack([],0)
        return res
    