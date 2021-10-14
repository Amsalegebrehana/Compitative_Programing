#leet code 415 Add string Solution

def addString(numS1, numS2):
    if int(num1)>=0 and int(num2)>=0 and 1 <=len(num1) and len(num2)<= math.pow(10,4):
            if num1.isdigit() and num2.isdigit() and num1[0] != 0 and num2[0] != 0:
                result = int(num1) + int(num2)
                return str(result)
print(addString("11","123"))