#leetcode length of last word solution 

def lenOfLastWord(s):
    s= s.strip()
    l = s.split(' ')
    lenLastWord = len(l[len(l)-1])
    print(lenLastWord)
    return l
print(lenOfLastWord("   fly me   to   the moon  "))