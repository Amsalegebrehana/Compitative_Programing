class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        res = 0
        l, lk = 0, 0
        dictt = dict()
        
        if k == 0 or len(nums) < k:
            return 0
     
        for right in range(len(nums)):
            
            dictt[nums[right]] = right
            
            if len(dictt) == k + 1:
                lk = min(dictt.values())
                dictt.pop(nums[lk])
                lk += 1
                l = lk
                
            if len(dictt) == k:
                lk = min(dictt.values())
                res += lk - l + 1
                
                
        return res