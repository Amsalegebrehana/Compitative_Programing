#leetcode Pow() solution 

def pow(x,n):
    result = 1 
    for i in range(0,abs(n)):
        result *= x
    if n >= 0:
        return result
    else:
        result = 1/ result
        return result  
print(pow(2.0000, -2))