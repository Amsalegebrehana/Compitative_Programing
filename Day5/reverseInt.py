


import math
def reverse(x):
    if int(math.pow(-2,31)) <= x <= int(math.pow(2,31) -1):
        result=''#to append the reverse iterated numbers 
        while x  % 10 == 0 and x!=0:
            x= x//10
        strNum = str(x)# convert the given number to string
        if strNum[len(strNum)-1] == '0' and len(strNum) > 1: #to eliminate zero if the length 
            strNum = strNum[:len(strNum)-1]
        if strNum[0]== '-': # slice out negative sign if there is any
            sliceNum= strNum[1:]

            for i in range(len(sliceNum)-1,-1,-1): #iterating the number from the last to the front 
                result += sliceNum[i]
            if int(math.pow(-2,31)) <= int(result) <= int(math.pow(2,31) -1): 
                return strNum[0] + result
            else:
                return 0

        else:
            for i in range(len(strNum)-1,-1,-1):
                result += strNum[i]
            if int(math.pow(-2,31)) <= int(result) <= int(math.pow(2,31) -1): 
                return int(result)
            else:
                return 0
            
    else:
        return 0
print(reverse(1000))
