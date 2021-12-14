


def plusOne(digits):
    
    x = ''
    l =[]
    for i in digits:
        x+=str(i)
    num = int(x) + 1
    
    while num > 0:
        b = num%10
        l.append(b)
        num = num //10
    return l[::-1]
print(plusOne([1,2,9]))