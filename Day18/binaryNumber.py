#hackerRank binary number reputation

def bunaryNum(num):
    
    l=''
    c = 0
    x=0
    h=''
    while num > 0:
        rem = num % 2
        num = num//2 
        l+=str(rem)
    print(l)
    if '0'  in l:
        while l[x] !='0' and x<len(l):
            h+=l[x]
            x+=1
    
        s = ''
        l=l[::-1]
        while l[c] !='0' and c<len(l):
            s+=l[c]
            c+=1
    else:
        c=len(l)
    if (x > c):
        return x
    else:
        
        return c
print(bunaryNum(5))