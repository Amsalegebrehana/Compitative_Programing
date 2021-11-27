num11 = "-132"
num22 = "22"

if num11[0] == '-':
    num1 = num11[1:]
else:
    num1 = num11

if num22[0] == '-':
   num2 = num22[1:]
else:
    num2 = num22
print(num1)
print(num2)
result = ""
r = []
h = []
for i in range(0 , len(num2)):
    result = str(int(num1) * int(num2[i]) ) 
    r.append(result)
j = 0
for i in range(len(r)-1 , -1, -1):
    x = i * '0' +  r[i]  + j *'0' # add zeros to the front and also to the back
    h.append(x)
    j += 1 #increment
sum = 0
for i in range(0, len(h)):
    sum += int(h[i])
if num11[0] == '-' and  num22[0] != '-' or num11[0] != '-' and  num22[0] == '-':
    print('-' + str(sum))
else:
    print( str(sum))