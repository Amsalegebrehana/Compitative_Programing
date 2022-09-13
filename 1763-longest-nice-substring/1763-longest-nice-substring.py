class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def dfs(s):
            sset = set(s)
            if len(s) < 2:
                return ""
            for i in range(len(s)):
                if not (s[i].lower()  in sset and s[i].upper()  in sset) :
                    s1 = dfs(s[:i])
                    s2 = dfs(s[i+1:])
                    return s1 if len(s1) >=  len(s2) else s2
            return s
        return dfs(s)