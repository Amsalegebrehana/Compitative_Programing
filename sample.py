num1 = input("enter n1 : ")
num2 = input("enter n2 : ")

len1 = len(num1)
len2 = len(num2)



if len1 == len2 :
    result = ''
    r = ''
    track = 0
    carry = 0
    for i in range(1, len1+1):
        n = ''
        
        # print("carry ",carry)
        # print("track ", track)
        if track == 1:
            print("debugg")
            if carry == 1:
                n += str(int(num1[len1-i]) - 1)
                print("n ",n)
                carry = 0
            if (int(n) < int(num2[len2-i])):
                print("debug 2")
                n1 = '1' + n
                result += str(int(n1) - int(num2[len2-i]))
                carry = 1
            elif (int(n) > int(num2[len2-i])):
                result += str(int(num1[len1-i]) - int(num2[len2-i]))
       
        else:
            print("debug1")
            track = 1
            if (int(num1[len1-i]) < int(num2[len2-i])):
                n1 = '1' + num1[len1-i]
                result += str(int(n1) - int(num2[len2-i]))
                carry = 1
            elif (int(num1[len1-i]) > int(num2[len2-i])):
                result += str(int(num1[len1-i]) - int(num2[len2-i]))
            
        
    for i in range(1,len(result)+1):
        r += str(result[len(result) - i])
    print(r)