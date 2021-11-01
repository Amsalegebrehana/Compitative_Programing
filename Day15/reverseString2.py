#leet code 521 Reverse String ll solution
# https://leetcode.com/problems/reverse-string-ii/
def reverseStr(s, k):
    h = ''
    if k < len(s):
        r = s[:k]
    else:
        r = s
    for i in range(len(r)-1,-1,-1):
        h += r[i]

    return h +s[k:]
   
print(reverseStr("abcdefg",2))