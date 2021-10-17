#leetcode 9 palindrome number
def isPalendrome(x):
    num = str(x)
    numP = ''
    if num[0] == '-':
        return False
    else:
        for i in range(len(num)-1,-1,-1):
            numP+=num[i]
        if int(numP) == int(num):
            return True
        else:
            return False
    print(numP)
    
print(isPalendrome(121))