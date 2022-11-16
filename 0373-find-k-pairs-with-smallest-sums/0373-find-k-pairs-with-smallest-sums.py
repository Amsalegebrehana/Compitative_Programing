class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        min_range = min(k, len(nums1))
        for i in range(min_range):
            heappush(heap, (nums1[i] + nums2[0],[nums1[i] , nums2[0]] , 0))
        result = []
     
        while k > 0 and heap:
            summ, pair, idx = heappop(heap)
            result.append(pair)
            if idx + 1 < len(nums2) :
                heappush(heap, (pair[0] + nums2[idx + 1], [pair[0] ,nums2[idx + 1]], idx+1))
        
            k-=1
        return result
        