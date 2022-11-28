class Solution:
    def canmerge(self, interval1, interval2):
        if interval1[1] >= interval2[0]:
            return True
        return False
            
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        pt1 = 0
        pt2 = 0
        len_f  = len(firstList)
        len_s = len(secondList)
        while pt1 < len_f and pt2 < len_s:
            it1, it2 = sorted([firstList[pt1], secondList[pt2]])
            if self.canmerge(it1, it2 ):
                result.append([max(it1[0], it2[0]), min(it1[1], it2[1])])
            if firstList[pt1][1] > secondList[pt2][1]:
                pt2 +=1
            else:
                pt1 +=1
        return result