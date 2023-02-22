class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictt = {}
        for i in range(len(s)):
            if s[i] not in dictt:
                
                if t[i] in dictt.values():
                    return False
                else:
                    dictt[s[i]] = t[i]
                
            elif s[i] in dictt: 
               
                if t[i] != dictt[s[i]]:
                   
                    return False
             
        return True
               