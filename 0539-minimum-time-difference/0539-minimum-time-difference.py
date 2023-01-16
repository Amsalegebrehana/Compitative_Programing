class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        size = len(timePoints)
        lasthr = 24 * 60
        
        for i in range(size):
            timePoints[i] = timePoints[i].split(":")
            timePoints[i] = (int(timePoints[i][0]) * 60) + int(timePoints[i][1])
            
        timePoints.sort()
        result = float("inf")
        for i in range(1, size):
            time_diff = timePoints[i] - timePoints[i-1]
            result = min( result , time_diff)
        time_diff = lasthr - timePoints[-1] + timePoints[0]
        result = min(result, time_diff)
        
        return result
        