class Solution:
    def maxJump(self, stones: List[int]) -> int:
        even = []
        odd = []
        for i in range(len(stones)):
            if i % 2 ==0:
                even.append(stones[i])
            else:
                odd.append(stones[i])

        odd.insert(0,stones[0])
        if (len(stones) -1) % 2 != 0:
            even.append(stones[-1])
        else:
            odd.append(stones[-1])

        lenf = 0
        pre = 0
        for i in even:
        
            lenf= max(lenf, abs(pre- i))
            pre = i
        lenb = 0
        pre = 0
        for i in odd:
       
            lenb= max(lenb, abs(pre- i))
            pre = i
  
        return max(lenf,lenb)
            
        