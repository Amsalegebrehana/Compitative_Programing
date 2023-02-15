class Solution:
    def checkValidString(self, s: str) -> bool:
      
        openn = []
        star = []
   
        for i in  range(len(s)):
            if s[i] == "(":
                openn.append(i)
            elif s[i] == "*":
                star.append(i)
            else:
                if openn:
                    openn.pop()
                elif star:
                    star.pop()
                else:
                    return False
      
        while openn and star:
            if openn[-1] > star[-1]:
                return False
            openn.pop()
            star.pop()
        return openn == []