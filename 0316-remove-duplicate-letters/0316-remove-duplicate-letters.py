class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letter_count = Counter(s)
        stack = []
        instack = set()
      
        for i in s:
            if not stack:
                stack.append(i)
                instack.add(i)
            else:
                while stack and i < stack[-1] and letter_count[stack[-1]] > 1 and i not in instack:
                    letter_count[stack[-1]] -=1
                    
                    instack.remove(stack.pop())
                if i not in instack:
                    stack.append(i)
                    instack.add(i)
                else:
                    letter_count[i] -=1
       
        return "".join(stack)
        
    