class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        currmax = 0
        ans = -1
        freq = Counter(nums)
        for i in freq:
            if i % 2 == 0:
                if freq[i] > currmax or (currmax == freq[i] and i < ans):
                    currmax = freq[i]
                    ans = i
        return ans
                