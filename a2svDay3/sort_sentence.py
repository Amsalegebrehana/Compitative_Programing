#leetcode
def sortingsent(s):
    s1 = s.split(' ')
    for i in s1:
        print(i[-1])
        c=1
        for j in range(0,len(s1)):
            if i[-1] == c:
                pass
            
    return s1
print(sortingsent("is2 sentence4 This1 a3"))