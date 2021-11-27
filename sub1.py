num1 = "1"
num2 = "255"
result = ""
len1 = len(num1)
len2 = len(num2)
b = 0
if len1 >= len2:
    h = len1 - len2
    num2 = h * '0' + num2 # add infront of a number to make it equal length as the other one
    len2 = len(num2)
elif len2 > len1:
    h = len2 - len1
    num1 = h * '0' + num1 # add infront of a number to make it equal length
    len1 = len(num1)
if int(num1) >= int(num2):
    for i in range(len1-1, -1,-1):
        
        if num1[i] < num2[i]:
            result += str((int(num1[i]) + 10 - int(num2[i])) - b)
            b = 1
        elif num1[i] > num2[i] and b==0:
            result += str((int(num1[i]) - int(num2[i])) )
        elif num1[i] > num2[i] and b==1:
            result += str((int(num1[i]) - int(num2[i])) - b )
            b = 0
    print(result[::-1])
elif int(num1) < int(num2):
     #  swap here is just not rewrite again
    print(num1)
    temp = num1
    num1 = num2
    num2 = temp
    print(num1)
    print(num2)
    for i in range(len1-1, -1,-1):
        
        if num1[i] < num2[i]:
            result += str((int(num1[i]) + 10 - int(num2[i])) - b)
            b = 1
        elif num1[i] > num2[i] and b==0:
            result += str((int(num1[i]) - int(num2[i])) )
        elif num1[i] > num2[i] and b==1:
            result += str((int(num1[i]) - int(num2[i])) - b )
            b = 0
    print('-' + (result[::-1]))
# print(result[::-1])