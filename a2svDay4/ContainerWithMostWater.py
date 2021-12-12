


def water(height):
    l=[]
    p=1
    l2=list(set(height))
    print(l2)
    for i in range(0,len(l2)):
        p= i* l2[i]
        l.append(p)
    print(l)
    return max(l)

print(water([1,8,6,2,5,4,8,3,7] ))
    