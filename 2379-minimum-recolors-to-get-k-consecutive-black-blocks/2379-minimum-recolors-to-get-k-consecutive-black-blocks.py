class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        mincount = len(blocks)
        count = 0
        i = 0
        for j in range(len(blocks)):
            if blocks[j] == 'W':
                count +=1
            if j - i + 1 == k:
                mincount = min(count, mincount)
                if blocks[i] == 'W':
                    count-=1
                i +=1
        return mincount