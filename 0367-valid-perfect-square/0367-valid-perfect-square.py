class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = num
        left = 1
        while left <=  n:
            mid = (left + n)//2
            if mid * mid > num:
                n = mid - 1
            elif mid * mid < num:
                left = mid + 1
            else:
                return True
        return False
                
            
        