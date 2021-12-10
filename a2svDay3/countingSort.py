#hackerrank counting sort algorithm

def countingSort(arr):
   
    l=[]
    # l2=[]
    for i in range(6):
        l.append(0)
    print(l)
    for j in arr:
        for i in range(0,len(l)):
            if j == i:
                l[i] +=1
                
        
            
                print(i)
    
    # print(l2)   
    return l 
print(countingSort([1,4,2,2,3]))