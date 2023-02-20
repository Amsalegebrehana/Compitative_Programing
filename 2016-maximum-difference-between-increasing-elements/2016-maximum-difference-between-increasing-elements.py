class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    max_diff = max(max_diff, nums[j] - nums[i])
        return max_diff 