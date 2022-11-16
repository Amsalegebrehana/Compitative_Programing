class Solution:
    def romanToInt(self, s: str) -> int:
        dictt = {"I": 1, "V": 5,"X":10, "L": 50, "C":100, "D":500, "M":1000}
        
        prev = s[len(s)  - 1]
        res = 0
        i = len(s) - 1
        while i >= 0:
          
            if dictt[s[i]] >= dictt[prev]:
            
                res += dictt[s[i]]
            else:
                res -= dictt[s[i]]
            prev = s[i]
            i -=1
                
        return res