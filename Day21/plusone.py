#leetcode plus one solution 

def plusOne(digits):
    l=[]
    last = digits[len(digits)-1] + 1
    if last < 10:
                      
        digits[:] = digits[:len(digits)-1]
        digits.append(last)
    else:
        b = last
        while b >= 10:
            a = last %10 
            b = b // 10 
            l.append(a)
        l.insert(0,b)
        print(l)
        print(last)
        # if len(l) > 1:
        list2 = []
        digits[-1] = 0
       
        for i in range(len(l)):
            k = l[i] + digits[i]
            list2.append(k)
                
        print("list2", list2)
    return digits
    
    
    
print(plusOne([3,2,9]))
    