num1 = "2769"
num2 = "1879"
l = []
l2 = []
result = []
len1 = len(num1)
len2 = len(num2)
for i in num1:
    l.append(i)
for i in num2:
    l2.append(i)
print(l)
print(l2)
r = 0
if len1 == len2:
    if int(num1) >= int(num2):
        for i in range(0,len1):
            if int(l[i]) >= int(l2[i]):
                
                r = (int(l[i])) - int(l2[i])
            c = 0
            if int(l[i]) < int(l2[i]) :
                r = (int(l[i]) + 10) - int(l2[i])
                c = 1
                if int(l[i]) < int(l2[i]) and c == 1:
                    r = (int(l[i]) -1 + 10) - int(l2[i])
                    c = 1
            elif int(l[i]) >= int(l2[i]) and c == 1:
                r = (int(l[i]) -1) - int(l2[i])
                c = 0
            elif int(l[i]) >= int(l2[i]) and c == 0:
                r = (int(l[i])) - int(l2[i])
            
        # for i in range (0, len1):
            

            
            # if int(l[i]) < int(l2[i]):
               
                # print(r)
            #     if i + 1 < len1:
            #         l[i] = int(l[i]) - 1
            #         c = 0
            #         print(l[i])
            #     r = (int(l[i]) + 10) - int(l2[i])
            #     c=1
            #     if int(l[i]) >= int(l2[i]) :
            # #     for i in range(0,len1):
            #       r = (int(l[i])  - int(l2[i]))
            result.append(r)
        print(result)    