class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9) + 7
        if n == 1:
            return 5
        # if n %2 == 0:
        div = n //2
        return (pow( 4,div,mod) * pow(5,div+n%2,mod))%mod
        # else:
        #     div1=n//2
        #     div2=n-div1
        #     return (div1*5)*(div2*4)