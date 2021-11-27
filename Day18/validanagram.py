#leetcode 242 valid anagram solution

def isAnagram(s,t):
    h = s
    ls=[]
    lt=[]
    ss = sorted(s)
    tt = sorted(t)
    for i in range(0, len(ss)):
        if ss[i] == tt[i]:
            return True
    print(ss)
    print(tt)
    # for i in s:
    #     ls.append(i)
    # print(ls)
    # for i in t:
    #     lt.append(i)
    # print(lt)
    # if len(s) == len(t):
    #     for i in lt:
          
    #         if i not in ls:
    #             h+=i
    #         else:
    #             idxt = lt.index(i)
    #             idxs = ls.index(i)
    #             ls.remove(ls[idxs])
    #             # lt.remove(lt[idxt])
                
      
    #     if len(h) - len(lt) == 0:
          
    #         return True
    #     else:
    #         return False
    # else:
    #     return False     
   
print(isAnagram("anagram", "nagaram"))
        
                