class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)-1
        left = 1
        right = size
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for i in nums:
                if i <= mid:
                    count +=1
            if count > mid:
                ans = mid
                right = mid -1
            else:
                left = mid + 1
        return ans
                
                
            
            
            
        
        
        