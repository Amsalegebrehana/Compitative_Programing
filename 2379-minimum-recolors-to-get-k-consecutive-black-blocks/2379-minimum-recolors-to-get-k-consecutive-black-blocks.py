class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = 0
        r = 0
        l = 0
        result = len(blocks)
        while r < len(blocks):
            if blocks[r] == "W":
                w += 1
            if r - l + 1 == k:
                result = min(result, w)
                if  blocks[l] == "W":
                    w -=1
                l+=1
            r += 1
        return result
                
                
            