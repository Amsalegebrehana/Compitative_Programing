


def difference(s,t):
    l=[]
    lt=[] 
    for i in s:
        l.append(i) 
    for i in t:
        lt.append(i) 
    print(l)
    print(lt)
   
    for i in l:
        if i in lt:
            lt.remove(i)
            l.remove(i)
        # else:
    
    
print(difference("aa","a"))