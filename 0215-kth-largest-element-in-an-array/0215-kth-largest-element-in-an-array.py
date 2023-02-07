class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, -num)
        
        ans = 0
        while k != 0:
            ans = -1 * heappop(heap)
            k -= 1
        return ans