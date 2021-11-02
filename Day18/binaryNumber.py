#hackerRank binary number reputation

def bunaryNum(num):
    
    l=''
    c = 0
    while num > 0:
        rem = num % 2
        num = num//2 
        l+=str(rem)
    s = ''
    l=l[::-1]
    while l[c] !='0' and c<len(l):
        s+=l[c]
        c+=1
   
    return c
print(bunaryNum(125))