#single number 

def singleNum(nums):
    l=[]
    j=[]
    last = 0
    while len(nums) > 0:
        x = nums.pop()
        if x not in l:
            l.append(x)
        else:
            j.append(x)
    for i in l:
        if i not in  j:
            last = i
            print("last", i)
            
    print(nums) 
    print(j)  
     
    print(x)      
    print(l)  
    return last
print(singleNum([1]))