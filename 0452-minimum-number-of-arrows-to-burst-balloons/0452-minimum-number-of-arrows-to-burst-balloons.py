class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point:point[1])
        count = 1
        currpair = points[0][1]
   
        for i,j in points:
            if i > currpair:

                currpair  = j

                count+=1
                  
        return count