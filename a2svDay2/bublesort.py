#hacker rank buble sort solution
def countSwaps(a):
    # Write your code here
    n=len(a)
    count = 0
    for i in range(0, n):
        for j in range(0, n-1):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1],a[j]
                count+=1
    print("{}".format(count))
    return count
                
print(countSwaps([1,2,3]))