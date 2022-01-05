

arr=[1,2,3,4,5,6]
l=[]
k=5
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        x= arr[i] + arr[j]
        print(x)
        if i< j and x % k == 0:
            print("here")
            l.append([arr[i],arr[j]])
print(l)
print(len(l))
        
    