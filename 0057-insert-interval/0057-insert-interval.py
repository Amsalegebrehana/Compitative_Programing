class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        position = bisect.bisect(intervals, newInterval)
        # O(N)
        intervals.insert(position, newInterval)
        result = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1] = [result[-1][0], max(result[-1][1], intervals[i][1])]
            else:
                result.append(intervals[i])
        
        return result