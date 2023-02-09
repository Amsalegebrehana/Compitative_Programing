class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num = [int(i) for i in str(num)]
        max_idx = len(num) - 1
        pt1 = pt2 = 0
        
        for i in range(len(num) - 1, -1, -1):
            
            if num[i] > num[max_idx]:
                max_idx = i
            elif num[i] < num[max_idx]:
                pt1 = i
                pt2 = max_idx
        num[pt1], num[pt2] = num[pt2], num[pt1]
        
        return int(''.join([str(i) for i in num]))
        