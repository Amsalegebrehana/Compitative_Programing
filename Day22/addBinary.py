
#leetcode 67 Add binary solution 

def addBinary(a,b):
    s = ""
    lendiff = len(a) -len(b)
    if lendiff < 0:
        a = abs(lendiff) * "0" + a
    else:
        b = abs(lendiff) * "0" + b
    print(b)
    print(a)
    carry = 0
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1' and carry == '0':
            s+='0'
            carry = 1 
        elif a[i] == '1' and b[i] == '1' and carry = '1':
             s+='1'
            carry = 1 
        elif a[i] == '1' and b[i] == '1' and carry = '1':
            s+='1'
            carry = 1 
            
    return lendiff 

print(addBinary("11","1"))