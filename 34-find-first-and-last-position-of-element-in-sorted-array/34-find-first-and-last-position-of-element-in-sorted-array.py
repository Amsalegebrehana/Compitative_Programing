class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        bestl = -1
        bestr = -1
        left = 0
        right = len(nums) -1 
        while left <= right:
            mid = (left + right) // 2
           
                
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                bestl = mid 
                right = mid -1
       
        left = 0
        right = len(nums) -1 
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                bestr = mid
                left = mid + 1
       
        return [bestl, bestr]
                
                
            