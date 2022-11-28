class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = 10 ** 9
        best = 0
        while left < right:
            mid = ((left + right) // 2)
            curr = 0
           
            for i in range(len(nums)):
                curr += ((nums[i]-1) // mid)
           
            if curr > maxOperations:
    
                left = mid + 1
            else:
               
                right = mid 
                
        return left
            