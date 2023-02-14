class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        ns = [int(i) for i in str(n)]
    
        ns.sort()
        for i in range(30):
            temp = []
           
            for j in str( 2**i):
                temp.append(int(j))
            temp.sort()
            if temp == ns:
                return True
        return False