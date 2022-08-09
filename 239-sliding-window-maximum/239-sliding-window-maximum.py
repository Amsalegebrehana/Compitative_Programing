class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        heap = []
        result = []
        for right in range(len(nums)):
            heappush(heap,(-1 * nums[right], right))
            if right - left + 1 == k:
                while heap[0][1] < left:
                    heappop(heap)  
                result.append(-1 * heap[0][0])   
                left += 1
        return result
                
            
        