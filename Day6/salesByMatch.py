#hacker rank sales by match solution 
def salesByMatch(n, ar):
    numPairs = 0
    paired = False
    arSet = set([])
   
    for i in range(n):
        if ar[i] in arSet:
            numPairs +=1
            arSet.remove(ar[i])# if found in the set remove it from the set to prevent from counting again
        else:
           
            arSet.add(ar[i])

    return numPairs 
print(salesByMatch(10,[1, 1, 3, 1, 2,1, 3, 3, 3, 3]))
