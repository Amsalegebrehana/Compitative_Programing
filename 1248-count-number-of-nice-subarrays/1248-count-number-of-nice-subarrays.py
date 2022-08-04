class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_odd_count = defaultdict(int)
        prefix_odd_count[0] = 1
        res = prefix_odd = 0 
        for num in nums:
            if num % 2 == 1:
                prefix_odd += 1
            if prefix_odd - k in prefix_odd_count:
                res += prefix_odd_count[prefix_odd - k]
            prefix_odd_count[prefix_odd] += 1
        return res