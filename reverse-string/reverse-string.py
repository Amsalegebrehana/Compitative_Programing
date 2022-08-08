class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) -1        
        def recursion(l,r):
            if l < r:
                s[l],s[r]=s[r],s[l]
                recursion(l+1, r-1)
        
        recursion(l,r)
            
            