

#leetcode mean array

def meanArr(arr):
    s =0
       
    lr=int(len(arr)*0.05)
    arr[:]=sorted(arr)
    l=arr[lr:-lr] 
    
    
    for i in range(0, len(l)):
        s+=l[i]
    print(s)
    print(len(l))
    return sum(l) /len(l)
print(meanArr([6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))