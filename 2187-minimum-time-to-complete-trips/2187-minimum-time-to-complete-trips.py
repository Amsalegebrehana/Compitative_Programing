class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
       
        left = 1
        right = totalTrips  * min(time)
        best = 0
        while left <= right:
            mid = (left + right) // 2
            curr = 0
            for i in range(len(time)):
                curr += (mid // time[i])
            if totalTrips > curr:
          
                left = mid + 1
            else:
                right = mid   -1 
        
        return left