#leetcode group anagram

def grp_anagram(strs):
    strs2= []
    for i in strs:
        for j in range(0,len(i)):
            strs2.append(sorted(i[j]))
    print(strs2)
    
print(grp_anagram(["eat","tea","tan","ate","nat","bat"]))