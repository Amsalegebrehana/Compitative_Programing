num1 = "132"
num2 = "22"
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
print(sum)
