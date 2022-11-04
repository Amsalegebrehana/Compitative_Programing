class Solution:
    def countPrimes(self, n: int) -> int:
        
        isPrime = [True] * n
        count = 0
        if n == 0 or n == 1:
            return 0
        isPrime[0] = False
        isPrime[1] = False
        for i in range(2,n):
            if i * i <= n:
                if isPrime[i]:
                
                    for j in range(i + i, n, i):
                        isPrime[j] = False
           
        return isPrime.count(True)