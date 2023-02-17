class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = ""
        res = []
        def backtrack(n,l,r,s, res):
            if l == n and r == n:
                res.append(s)
            else:
                if l < n:
                    backtrack(n, l+1, r, s + "(", res)
                if r < l:
                    backtrack(n, l, r + 1, s + ")", res)

        backtrack(n,0,0,s,res)

        return res