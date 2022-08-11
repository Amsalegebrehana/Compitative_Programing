class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        left = right = len(nums) - 1
        
        currSum = nums[right]
        while left >= 0:
            
            if nums[right]  *  (right - left + 1) > currSum + k:
                
                currSum -= nums[right]
                count = max(count, right - left )
                right -= 1
            left -= 1
            currSum += nums[left]
        count = max(count, right - left )
           
        return count
            
            
        
                
            
        
        
        