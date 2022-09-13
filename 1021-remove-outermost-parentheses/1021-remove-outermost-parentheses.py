class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stk = []
        ans = ""
        for i in s:
            if i == '(':
                if len(stk) == 0:
                    stk.append('(')
                else:
                    ans +='('
                    stk.append('(')
            else:
                if len(stk) == 1:
                    stk.pop()
                else:
                    ans+=')'
                    stk.pop()
        return ans
        