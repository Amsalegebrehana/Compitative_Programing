class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        ans = ""
        pt1 = len(a) - 1
        pt2 = len(b) - 1
        carry = 0
        while pt1 >= 0 or pt2 >= 0 or carry:
            if pt1 >= 0:
                carry += int(a[pt1])
            else:
                carry += 0 
            if pt2 >= 0:
                 carry += int(b[pt2])
            else:
                carry += 0
            
            ans = str(carry % 2) + ans
            carry = carry // 2
            pt1 -= 1
            pt2 -= 1
            
        return ans
        