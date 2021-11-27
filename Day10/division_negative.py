
def div(num1 , num2):
    # result= ''
    trysubstr = ''
    #first if the number is greater than the divider
    if str(num1)[0] == '-' and str(num2)[0] != '-':
        num1 = int(str(num1)[1:])
        result = '-'
    elif str(num2)[0] == '-' and str(num1)[0] != '-':
        num2 = int(str(num2)[1:])
        result = '-'
    elif str(num2)[0] == '-' and str(num1)[0] == '-':
        num1 = int(str(num1)[1:])
        num2 = int(str(num2)[1:])
        result = ''
    if num1 < num2:
        # no need to check the length just add 0 at the end
        num1s = str(num1) + '0'
        num1 = int(num1s)
        result += '0.'
        print(num1)
    else: 
        num1 = num1
        result += ''
    print(str(num1)[:len( str(num2))])
    
    while num1 >= num2:#12 / 10
        if len(str(num1)) >= len( str(num2)) :
            trydiv = num1//num2
            trymulti = trydiv * num2
            print("trymulti",trymulti)

            trysub = num1 - trymulti
            print("trysub",trysub)
            result += str(trydiv)
            if trysub < num2 and trysub != 0:
                trysubstr = str(trysub) + '0'
                print(trysubstr)
                num1 = int(trysubstr)
                if '.' not in result:
                    result += '.'
            else:
                num1 = trysub
  
    print(num2)
    print(num1)
    return result
print(div(122 , -122))