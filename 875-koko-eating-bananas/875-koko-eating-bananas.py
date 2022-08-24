class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(mid):
            summ = 0
            for i in piles:
                
                summ += math.ceil(i / mid)
               
            return summ
        left = 1
        right = max(piles)
      
        while left <= right:
            mid = (left + right)// 2
            if helper(mid) > h :
              
                left = mid + 1
                
            else:
               
                right = mid - 1
               
        return left