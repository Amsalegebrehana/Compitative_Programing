class Solution:
    def findComplement(self, num: int) -> int:
        val = 0
        og = num
        while (1<<val) <= og:
            num = num ^ (1<<val)
            val+=1
        return num