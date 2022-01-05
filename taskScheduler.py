# leetcode task scheduler solution

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        Dict = Counter(tasks)
        h=Dict.most_common()
        s= sum(Dict.values())
        f=h[0][1]
        r = f + (f-1)*n
        i=0
        c=0
        while i < len(h):
            if h[i][1] == f:
                c+=1
            i+=1
        if c > 1:
            while c>1:
                r+=1
                c-=1
        return max(s,r)
        