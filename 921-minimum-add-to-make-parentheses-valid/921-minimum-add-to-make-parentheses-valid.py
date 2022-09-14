class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        for i in s:
            if i ==')' and (not stk or stk[-1] == ')'):
                stk.append(i)
            elif i == ')' and stk[-1] =='(':
                stk.pop()
            else:
                stk.append(i)
       
        return len(stk)