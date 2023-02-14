class Solution:
    def sumZero(self, n: int) -> List[int]:
   
        ans = []
        num = (n // 2) + 1
        for i in range(num):
            if i != 0:
                ans.append(-i)
                ans.append(i)
        if len(ans) != n:
            ans.append(0)
        return ans
            
        