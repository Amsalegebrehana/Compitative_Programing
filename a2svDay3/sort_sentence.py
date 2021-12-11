#leetcode
def sortingsent(s):
    s1 = s.split(' ')
    s2=[]
    for i in s1:
        for j  in s1:
            if i[-1] < j[-1]:
                # s1[i] , s1[j] = s1[j], s1[i]
                print(i)
                s2.append(i)
                # c = s1.index(i)
                # s1.remove(cd)
    print(s2)
    return s1
print(sortingsent("is2 sentence4 This1 a3"))