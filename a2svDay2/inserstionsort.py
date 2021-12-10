#hacker rank insertion sort part one solution

def insertionSort(n, arr):
    # for i in range(1,n):
    temp = arr[-1]
    j = n-1
    while j >0 and arr[j-1]>temp:
        arr[j] = arr[j-1]
        j-=1
        print(*arr)
    arr[j] = temp 
    print(arr)
    
    return arr 
print(insertionSort(5,[2, 4, 6, 8, 3]))