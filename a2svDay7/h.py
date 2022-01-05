

def h(arr):
    arr.sort()
    Dict = {}
    l=[]
    for i in range(0,len(arr)-1):
        Dict[(arr[i],arr[i+1])] = arr[i+1]-arr[i]
    minm= min(Dict.values())
    print(Dict.values())
    for i in Dict:
        if Dict[i] == minm:
            l.append(i)
    print(l)
    print(minm)
    print(Dict)
    x=[]
    for i in l:
        for j in range(len(i)):
            print(i[j])
            x.append(i[j])
    print(x)
            
h([5, 4, 3, 2])