

def uniquechar(s):
    h=''
    for i in s:
        if i in h:
            return False
        h+=i
def longestSubstr(s):
    sub=''
    r=0
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            sub = s[i,j+1]
            if uniquechar(sub):
                r = max(r,len(sub))
    return r
print(longestSubstr("pwwkew"))