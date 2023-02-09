class Solution:
   

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        
        def helper(s):
            return s == str(int(s)) and int(s) <= 255
        
        for i in range(1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if helper(a) and helper(b) and helper(c) and helper(d):
                        ans.append(a + "."+ b + "."+ c + "."+ d)
        return ans