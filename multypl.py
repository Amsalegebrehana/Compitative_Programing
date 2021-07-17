l = [1,1,5]
l2 = [2]
h = []
h2= []
b = 0
if len(l) > len(l2) and len(l2) == 1:

    for i in range(len(l) -1, -1,-1):
        for j in range(len(l2) -1, -1,-1):
            x = (l[i] * l2[j]) +b
            r = x % 10
            b = x//10
            # x += b
            print(b)
        h.append(r)
        print(h)
elif len(l) == len(l2) and len(l2) == 1:
    for i in range(len(l) -1, -1,-1):
        x = l[i] * l2[i]
        h.append(x)
    print(h)
'''
working multiplication
'''
num1 = "132"
num2 = "22"
len2 = len(num2) 
result = ""
print(result)
r = []
h = []
len1 = len(result)
d = []
for i in range(0 , len2):
    result = str(int(num1) * int(num2[i]) ) 
    r.append(result)
j = 0
for i in range(len(r)-1 , -1, -1):
    x = i * '0' +  r[i]  + j *'0' # add zeros to the front and also to the back
    h.append(x)
    j += 1 #increment
    # print(j)
sum = 0
for i in range(0, len(h)):
    # print(h[i])
    sum += int(h[i])
print(sum)

# print(h)
# print(d)