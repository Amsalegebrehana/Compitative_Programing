class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X','') != end.replace('X',''):return False
        Lstart = [i for i in range(len(start)) if start[i] == 'L']
        Rstart = [i for i in range(len(start)) if start[i] == 'R']
        Lend = [i for i in range(len(end)) if end[i] == 'L']
        Rend = [i for i in range(len(end)) if end[i] == 'R']
        i , j = 0, 0
        while i < len(Lstart):
            if Lstart[i] < Lend[i]:
                return False
            i+=1
        while j < len(Rstart):
            if Rstart[j] > Rend[j]:
                return False
            j+=1
        return True