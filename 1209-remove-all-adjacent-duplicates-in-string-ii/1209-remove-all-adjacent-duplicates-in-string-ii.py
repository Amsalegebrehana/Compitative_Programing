class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        store = defaultdict(int)
        
        for ch in s:
         
            store[ch] += 1
            stack.append(ch)
           
            if store[ch] >= k:
               
                dupl_len = set(stack[len(stack) - k : ] )
        
                if len(dupl_len) == 1:
                    for i in range(k):
                        stack.pop()
                    store[ch] -= k
  
        return "".join(stack)