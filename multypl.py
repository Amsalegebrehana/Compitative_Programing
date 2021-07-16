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