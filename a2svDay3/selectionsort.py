#geeks for geeks solution

def select(arr, i):
     # for j in range(i+1, len(arr)):
        
    #     min_nums = min(arr[j:])
    min_nums = min(arr[i:])
   
    return min_nums

def selectionSort(arr,n):
    c=0
    for i in range(c,n):
        minum = select(arr, c)
        idx = arr.index(minum)
        arr[i], arr[idx] = arr[idx] , arr[i] 
        c+=1
        print(arr)
        # for i in range(n):
        #     minum = self.select(arr, i)
        #     idx = minum
        #     arr[i], arr[idx] = arr[idx] , arr[i] 
        # return arr
    return arr 
print(selectionSort([4, 1, 3, 9, 7], 5))

        
        
        
        
        