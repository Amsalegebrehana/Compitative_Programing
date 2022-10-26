class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        left = 0
        right = len(part) - 1

        while right < len(s):
            if s[left: right + 1] == part:
                s =  s[:left] + s[right + 1:]
                left = 0
                right = len(part) - 1
            else:
                left += 1
                right += 1
        return  s
        
        