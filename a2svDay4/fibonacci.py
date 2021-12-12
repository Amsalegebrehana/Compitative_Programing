

#leetcode fibonacci
 
def fibonacci(n):
    sum = 0
    l=[]
    for i in range(0,n+1):
        
        if i == 0:
            sum = 0
            l.append(sum)
        elif i == 1 :
            sum = 1
            l.append(sum)
        # print(l)
    # print(l[1])
        else:
            sum = l[i-1] + l[i-2]
            l.append(sum)
    return l[n]
print(fibonacci(3))