#leetcode kClosest solution
import math
def kClosest(points,k):
    d = 1
    l = []
    l2=[]
    Dict = {}
    for i in points:
        # print(i[0])
        d= ((0-i[0])**2 + (0-i[1])**2)
        l.append(d)
        print(d)
    for i in range(0, len(points)):
        
        if l[i] not in Dict:
             
            Dict[l[i]] = [points[i]]
        else:
            Dict[l[i]].append(points[i])
       
    
    # for i in range(0, len(l)):
    #     for j in range(0, len(l)):
    #         if l[i] < l [j]:
    #             l[i],l[j] = l[j],l[i]
    l.sort()
    print(l)
    i = 0
    count= 0
    while i < k:
        h = Dict[l[i]]
        for j in range(0, len(h)):
            if count < k:
                l2.append(h[j])
                count +=1
            else:
                break
        i+=1
        # del Dict[l[i]]
    # print(l2)
    print(Dict)
    return l2
print(kClosest([[0,1],[1,0]],2))
   