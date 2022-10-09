class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count, left, right = 0, 0, 0
        result = 1
        if k <=1:
            return 0
        while right < len(nums):
            result *= nums[right]
            while left < len(nums) and result >= k:
                result = result // nums[left]
                left += 1
            count += (right - left + 1)
            right +=1
        
        return count
            
        