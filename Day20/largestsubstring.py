# leet code 3 largest sub string solution

def largeSubString(s):
    # s2 = ''
    # l=[]
    # if s == " ":
    #     return 1
    # for i in s:
    #     if i in s2:
    #         idx = s.index(i)
    #         # s2 += ' ' + i
    #         h = s[idx:]
    #         # print(h)
    #         print(idx)
    #     elif i not in s2:
    #         s2 += i 
       
    # l = s2.split(' ')
    # print(s2, end='')
    # j = []
    # for i in l:
    #     # mx = max(len(i))
    #     j.append(len(i))
    #     print(i)
    # mx = max(j) 
    # print(j)
    # print(mx)
    # return mx
    s2 = ''
    l=[]
    for i in range(len(s)):
        if s[i ] in s2:
            l.append(s[i:])
            print(i)
           
        else:
            s2 += s[i]
    print(l)
            
print(largeSubString("abcabcbb"))
        