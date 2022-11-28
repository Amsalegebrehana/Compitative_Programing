class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
      
        candies.sort()
        if sum(candies) < k:
            return 0
       
        left = 0
        right = sum(candies)
    
        best = 0
        while left <= right:
            curr = 0
            mid = math.ceil((left + right) / 2)
            for i in range(len(candies)):
                curr += (candies[i]// mid)
            if curr >= k:
                best = mid
                left = mid + 1
            elif curr < k:
                right = mid - 1
         
        return best