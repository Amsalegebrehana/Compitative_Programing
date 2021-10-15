#hacker rank sales by match solution 
def salesByMatch(n, ar):
    numPairs = 0
    paired = False
    arSet = set([])
    l=[]
   
    for i in range(n):
        if ar[i] in l:
            numPairs +=1
            l.remove(ar[i])# if found in the set remove it from the set to prevent from counting again
        else:
           
            l.append(ar[i])

    return numPairs 
print(salesByMatch(10,[1, 1, 3, 1, 2,1, 3, 3, 3, 3]))
