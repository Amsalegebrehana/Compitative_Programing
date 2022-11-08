class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for i in range(len(nums)):
            res = res ^ nums[i]

        res &= -res
 
        ans = [0,0]
        for i in nums:
            if res & i:
                ans[0] = ans[0] ^ i
            else:
                ans[1] = ans[1]  ^ i
        return ans