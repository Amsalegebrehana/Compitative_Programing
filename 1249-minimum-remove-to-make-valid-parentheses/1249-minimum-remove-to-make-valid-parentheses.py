class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = []
        count = 0
        for i in s:
            if i != ')':
                if i == '(':
                    count +=1
                l.append(i)
            elif i == ')' and count > 0:
                l.append(i)
                count -=1

        cb = 0
        queue = deque()
        for i in range(len(l)-1, -1, -1):
            if l[i] != '(':
                if l[i] == ')':
                    cb += 1
                queue.appendleft(l[i])
            elif l[i] == "(" and cb > 0:
                queue.appendleft(l[i])
                cb -=1
      
                
        return "".join(queue)