class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        runsum = 0
        min_len= inf
        
        while left < len(nums) and right < len(nums):
            runsum += nums[right]
      
            while runsum >= target:
                min_len = min(min_len, right - left + 1)
            
                runsum -= nums[left]
                left +=1
               
            
            right +=1
        return min_len if min_len != inf else 0