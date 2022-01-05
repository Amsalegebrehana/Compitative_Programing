

def x(h1,h2,h3):
    s1=[h1[-1]]
    s2= [h2[-1]]
    s3=[h3[-1]]
    for i in range(len(h1)-2,-1,-1):
        s=s1[-1] + h1[i]
        s1.append(s)
  
    for i in range(len(h2)-2,-1,-1):
        s=s2[-1] + h2[i]
        s2.append(s)
  
    for i in range(len(h3)-2,-1,-1):
        s=s3[-1] + h3[i]
        s3.append(s)
    print(s1)
    print(s2)
    print(s3)
    
    h = list(set.intersection(set(s1),set(s2),set(s3)))
    print(h)
    print(h[-1])
    return h[-1]
x([1,2,1,1],[1,1,2],[1,1])