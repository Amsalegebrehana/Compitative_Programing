class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        if start.replace('_','') != target.replace('_',''): return False

        Lstart = [i for i in range(len(start)) if start[i] == 'L']
        Rstart = [i for i in range(len(start)) if start[i] == 'R']
        Ltarget = [i for i in range(len(target)) if target[i] == 'L']
        Rtarget = [i for i in range(len(target)) if target[i] == 'R']
        i = 0
        j = 0
        while i < len(Lstart):
           
            if Lstart[i] < Ltarget[i]:
                return False
            i+=1
        while j < len(Rstart):
            if Rstart[j]> Rtarget[j]:
                return False
            j+=1
        return True
            
        
        