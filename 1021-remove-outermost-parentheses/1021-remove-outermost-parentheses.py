class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stk = []
        ans = ""
        for i in s:
            if i == '(':
                if not stk:
                    stk.append(i)
                else:
                    ans +="("
                    stk.append(i)
            else:
                if len(stk) == 1:
                    stk.pop()
                else:
                    ans +=")"
                    stk.pop()
        return ans
                    
                    