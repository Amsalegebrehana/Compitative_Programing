class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
      
        queue = deque()
        result = []
        for i in range(len(nums)):
            while queue and i - queue[0] + 1 > k:
                queue.popleft()
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i + 1 <k: continue
            result.append(nums[queue[0]])
        return result
        
                
            
        