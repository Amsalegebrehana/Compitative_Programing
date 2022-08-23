class Solution:
    def reverseVowels(self, s: str) -> str:
        vouwles = {'a','e','i','o','u', 'A','E','I','O','U'}
        lv = []
        for i in s:
            if i in vouwles:
                lv.append(i)
        j = 0
        lv = lv[::-1]
        l= [i for i in s]
        for i in range(len(l)):
            if l[i] in vouwles:
                l[i] = lv[j]
                j +=1
     
        return ''.join(l)