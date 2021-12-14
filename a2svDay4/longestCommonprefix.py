#leetcode longest common prefix

def prefix(strs):
    x=strs[0]
    s=''
    for i in strs:
        for j in range(0, len(x)):
            if x[j] in i:
                s+=x[j]
                print(s)
            
print(prefix(["flower","flow","flight"]))