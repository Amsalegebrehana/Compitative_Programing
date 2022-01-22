class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        half = (2**n -1) // 2
        k_idx = k % (half + 1)
        
        if k == half + 1:
            return '1'
        ans = self.findKthBit(n-1, k_idx if k_idx else 1)
        if k == (half + 1 ) + (2**(n-2)):
            return "0" if ans == "1" else "1"
        else:
            return ans
            