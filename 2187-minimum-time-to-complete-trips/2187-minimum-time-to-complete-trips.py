class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def helper(mid):
            bestmin = 0
            for i in time:
                bestmin += mid // i
            return bestmin 
        left = 1
        right = totalTrips * min(time)
        while left <= right:
            mid = (left + right) // 2
            if helper(mid) >= totalTrips:
                right = mid -1
            else:
                left = mid + 1
        return left
        