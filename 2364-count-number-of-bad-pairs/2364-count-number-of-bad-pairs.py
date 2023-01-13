class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
  
        count = 0
        n = len(nums)
       
        good = defaultdict(int)
        for i in range(n):
            count +=i - good[nums[i] - i]
            good[nums[i] - i] +=1

        return count
       
 
                
        