class Solution:
    def maximumProduct(self, heap: List[int], k: int) -> int:
        runp = 1
        heapify(heap)
        mod = (10 ** 9) + 7
        while k:
            num = heappop(heap)
            heappush(heap, num + 1)
            k -=1
 
        for i in heap:
            runp = (runp *i) % mod
        return runp 