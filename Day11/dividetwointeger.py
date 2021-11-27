# import math
#leetcode 29 divide to integer solution
def divide( dividend, divisor):
        div = 0
        if dividend < 0 and divisor < 0:
            dividend = abs(dividend)
            divisor = abs(divisor)
            r = 1
            
        elif dividend < 0 and divisor > 0:
            dividend = abs(dividend)
            r= -1
        elif dividend >= 0 and divisor < 0:
            divisor = abs(divisor)
            r=-1
        elif dividend >= 0 and divisor > 0:
            r=1
        elif dividend < divisor:
            return div
        if divisor == 1:
            div = dividend
           
        while dividend >= divisor and divisor != 1 and divisor != 0:
            dividend -= divisor
            div +=1
        return r*div


print( divide( -2147483648,-1))