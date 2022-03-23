# leetcode 763. Partition Labels

def Partition(s):
    dictt = {}
    for i in range(len(s)):
        dictt[s[i]] = i
    print(dictt)
    end = 0
    partitionsize = 0
    ans = []
    for i in range(len(s)):
        partitionsize +=1
        end = max(end, dictt[s[i]])
        if i == end:
            ans.append(partitionsize)
            partitionsize = 0
    return ans
            
        
        
print(Partition("ababcbacadefegdehijhklij"))
    