class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def checkpalndrome(start, end):
       
            temp = s[start:end]
            return  temp == temp[::-1]
              
        @lru_cache(None)
        def recursive(i):
            if i + k > len(s):
                return 0
            
            count = 0
            nexts = recursive(i + 1)
            if checkpalndrome(i, i + k):
                count =  max(count, 1 + recursive( i + k))
            if checkpalndrome(i , i + k + 1):
                count = max(count, 1 + recursive(i + k + 1))
                
            return max(nexts, count)
        return recursive(0)