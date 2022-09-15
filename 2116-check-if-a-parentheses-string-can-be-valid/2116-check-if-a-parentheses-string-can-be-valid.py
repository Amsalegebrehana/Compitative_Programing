class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        canFlip = 0
        openn = 0
        close = 0
        if len(s)%2 != 0:
            return False
        for i in range(len(s)):
            if locked[i] == '0':
                canFlip +=1
            elif s[i] == '(':
                openn+=1
            else:
                close +=1
            if canFlip + openn < close:
                return False
        canFlip = 0
        openn = 0
        close = 0
        for i in range(len(s)-1,-1,-1):
            if locked[i] == '0':
                canFlip +=1
            elif s[i] == '(':
                openn+=1
            else:
                close +=1
            if canFlip + close < openn:
                return False
        return True