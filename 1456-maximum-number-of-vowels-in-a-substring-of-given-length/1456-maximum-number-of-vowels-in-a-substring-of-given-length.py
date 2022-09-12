class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vset = {'a','e','i','o','u'}
        left = 0
        right = 0
        maxcount = 0
        count = 0
        while right < len(s):
            if s[right] in vset:
                count +=1
            if right - left + 1 == k:
                maxcount = max(maxcount, count)
                if s[left] in vset:
                    count-=1
                left += 1
            right +=1
        return maxcount