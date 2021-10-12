#leet code 374 guess number question solution

#this with O(n) time complexity

 for i in range(1,n):
            if guess(i) == 0:
                return i
        return n


#and this one is with  O(log(n))

left = 1
right = n
while left <= right:
    mid=(left+right)//2
    if guess(mid) == 0:
        return 0
    elif guess(mid) == -1:
        right = mid -1
    elif guess(mid) == 1:
        left = mid +1 
