#leetcode 557 Reverse Words in a string lll  solution
class Words:
    def __init__(self, s):
        self.s = s
    def reversWord(self):
        h=''
        k = ''
        l=[]
        for i in range(len(self.s)-1,-1,-1):
            h += self.s[i]
            # print(self.s[i], end='')
        # print(h.split())
        l=h.split()
        for i in range(len(l)-1,-1,-1):
            k+=l[i] + ' '
        print(k.strip())
word= Words("Let's take LeetCode contest")
word.reversWord()