class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        
        prefixsum = [0]
        for i  in range(len(w)):
        
            prefixsum.append(prefixsum[-1] + w[i])
        self.prefixsum = prefixsum[1:]

    def pickIndex(self) -> int:
        
        rand = random.randint(1,self.total)
        
        left = 0
        right = len(self.prefixsum ) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if self.prefixsum[mid] >= rand:
                right = mid
            else:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()