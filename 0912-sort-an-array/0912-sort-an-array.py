class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        result = []
        heapify(nums)
        while nums:
            temp = heappop(nums)
            result.append(temp)
        return result