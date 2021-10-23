
#leetcode 29 divide to integer solution
def divide( dividend, divisor):
        if str(dividend)[0] == '-' and str(divisor)[0] != '-':
            dividend = int(str(dividend)[1:])
            result = '-'
        elif str(divisor)[0] == '-'  and str(dividend)[0] != '-':
            divisor = int(str(divisor)[1:])
            result = '-'
        elif str(dividend)[0] == '-' and str(divisor)[0] == '-':
            divisor = int(str(divisor)[1:])
             
            dividend = int(str(dividend)[1:])
            result =''
            
        else:
            result = ''
        c = 0
        for i in range (dividend,-1,-divisor):
            if i >= divisor:
                c+=1
        
        return result + str(c)

print( divide( -1, -1))