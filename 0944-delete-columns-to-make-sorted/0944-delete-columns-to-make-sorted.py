class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        flag = False
        count = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
            
                if strs[j][i] > strs[j+1][i]:
                    flag = True
            if flag:
                count+=1
                flag = False
        return count