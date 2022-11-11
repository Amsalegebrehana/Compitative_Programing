class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        size = len(nums)
        nums.sort()
        diff = 0
        for i in range(size - 3, -1,-1):
            if nums[i] + nums[i+1]> nums[i+2]:
                diff = max(diff,nums[i] + nums[i+1] + nums[i+2])
        return diff