#leetcode implement srtStr() 28 solution

def strStr(haystack, needle):

    
    # for i in range(0, len(haystack)):
    #     print(needle[0])
    #     print(haystack[i])
    #     if needle[0] == haystack[i]:
    #         print(needle[0])
    #         return i
    #     else:
    #         return -1
    for i in haystack:
        if i == needle[0]:
            return haystack.index(i)
        
    return -1

     if  needle == "" or len(needle) > len(haystack) and needle[0] not in haystack and haystack != "":
            return 0
        else:
            needle = needle.lower()
            haystack = haystack.lower()
            if 0 <= len(haystack) and len(needle) <= 5 * 104:
                for i in haystack:
                    if i == needle[0] and len(needle) <= len(haystack):
                        return haystack.index(i)
            
                return -1
print(strStr("hello", "ll"))