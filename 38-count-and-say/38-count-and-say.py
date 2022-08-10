class Solution:
    def countAndSay(self, n: int) -> str:
        def counter(s):
            i = 0
            result = []
            for j in range(len(s)):
                if s[j] != s[i]:
                    result.extend([str(j - i), s[i]])
                    i = j
            result.extend([str(j - i + 1), s[i]])
            return ''.join(result)
        
        temp = '1'
        if n == 1:
            return temp
        for _ in range(1,n):
            temp = counter(temp)
        return temp
       
    