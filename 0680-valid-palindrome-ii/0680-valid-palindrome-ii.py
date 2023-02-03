class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) - 1
        def pali(s, left , right):
     
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
  
        while left <= right:

            if s[left] != s[right]:
                return pali(s, left + 1 , right) or pali(s, left , right-1)
            left += 1
            right -= 1
                
        return True
            