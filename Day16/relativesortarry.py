
#leetcode 1122 Relative Sort Array solution 

def relativeSortArr(arr1,arr2):
    arr3=[]
    
    for i in arr2:
        if i  in arr1:
            arr1.remove(i)
            arr3.append(i)
    
    for i in range(0,len(arr3)):
        if arr3[i] in arr1:
            arr1.remove(arr3[i])
            idx = arr3.index(arr3[i])
            arr3.insert(idx,arr3[i])
            print(idx)
    # print(arr3)
    arr1[:] = arr3 + sorted(arr1)
            
    return arr1
print(relativeSortArr([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))