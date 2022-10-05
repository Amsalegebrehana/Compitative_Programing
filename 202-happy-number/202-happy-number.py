class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            summ = 0
            seen.add(n)
            while n > 0 :
                summ += (n % 10) ** 2 
                n = n // 10
            n = summ
        return n == 1