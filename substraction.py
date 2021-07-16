def sub( number1 , number2):
    num1 = str(number1)
    num2 = str(number2)
    result = ""
    len1 = len(num1)
    len2 = len(num2)
    # n1 = []
    # n2 = []
    # for i in range(len1):
    #     n1.append(num1[i])
    # print(n1)
    # for i in range(len2):
    #     n2.append(num2[i])
    # print(n2)
    if len1 == len2:
        if int(num1) >= int(num2):
            for j in range(len1-1,0,-1):
                if num1[j] >= num2[j]:
                    for i in range(0,len1):
                        result += str(int(num1[i]) - int(num2[i]))
                    break
                elif num1[j] < num2[j]:
                    i = 0
                    f = 0
                    while i < len1:
                        # if f == 1:
                        #     s = int(num1[i]) - 1
                        #     print(type(s))
                        #     if str(s) < num2[i]:
                        #         x = int('1'+ str(s))
                        #         x1 = int(num2[i])
                        #         result += str ( x - )
                        #         # pass
                        #     elif str(s) > num2[i]:
                        #          result += str(( s - 1) - int(num2[i]))
                        #     else:
                        #         result += str(s - int(num2[i]))
                        # f = int(num1[i])

                        if num1[i] < num2[i]:
                            result += str(( int('1'+ num1[i])) - int(num2[i]))
                            f += 1
                        elif num1[i] < num2[i] and f == 1:
                            result += str(( int(num1[i]) - 1) - int(num2[i]))
                        elif num1[i] > num2[i]:
                            result += str(( int(num1[i]) - 1) - int(num2[i]))
                        else:
                            result += str(int(num1[i]) - int(num2[i]))

                        i+=1
                    break
        # else:
        #     pass

    return result


print(sub(2769,1879))