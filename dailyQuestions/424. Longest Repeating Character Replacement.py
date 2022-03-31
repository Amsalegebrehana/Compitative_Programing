

# 424. Longest Repeating Character Replacement

def lRepeatingchar(s,k):
    chardict = {}
    left = 0
    maxx = 0
    right = 0
    while right < len(s):
    
        if s[right] not in chardict:
            chardict[s[right]] = 1
        else:
            chardict[s[right]] += 1
        maxfreqchar = max(chardict.values())
        while (right - left + 1) - maxfreqchar > k:
            chardict[s[left]] -=1
            left+=1
        currwindow = right - left + 1
        maxx = max(maxx, currwindow)
        right += 1
    return maxx