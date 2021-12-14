

#leetcode Doubled Array solution

def doubledArray(changed):
    l2=[]
    changed.sort()
    x = len(changed)//2
    s = changed[:x]
    print(s)
    print(changed)
    for i in range(0, len(changed)):
        if changed[i] % 2 == 0:
            l2.append(changed[i])
            # changed.remove(i)
    return l2 
print(doubledArray([1,3,4,2,6,8]))