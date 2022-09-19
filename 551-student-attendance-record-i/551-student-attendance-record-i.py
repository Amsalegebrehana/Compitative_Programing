class Solution:
    def checkRecord(self, s: str) -> bool:
        cl,  ca, mxl = 0,0,0
     
        for i in s:
            if i == 'L':
                cl +=1
            elif i == 'A':
                ca +=1
                mxl = max(mxl,cl)
                cl = 0
            elif i == 'P':
                mxl = max(mxl,cl)
                cl=0
        mxl = max(mxl,cl)
        if mxl < 3 and ca < 2:
        
            return True
        else:
            return False
        