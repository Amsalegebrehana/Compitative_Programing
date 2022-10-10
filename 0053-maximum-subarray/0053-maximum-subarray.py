class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -float("inf")
        runsum = 0
        left = 0
        right = 0
        while right < len(nums) and left < len(nums):
            while nums[right]  >  runsum + nums[right]:
                runsum -= nums[left]
                left +=1
            runsum += nums[right]
            maxsum = max(maxsum, runsum)
            right +=1

        maxsum = max(maxsum, runsum)
        return maxsum