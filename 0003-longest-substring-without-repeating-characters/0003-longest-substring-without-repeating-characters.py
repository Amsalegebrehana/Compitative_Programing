class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        rundict = defaultdict(int)
        left = 0
        for i in range(len(s)):
            rundict[s[i]] +=1
            while len(rundict) < i - left + 1:
                max_len = max(max_len, i - left )
                if rundict[s[left]] > 0:
                    rundict[s[left]] -=1
                    if rundict[s[left]] == 0:
                            del rundict[s[left]]    
                left +=1

            max_len = max(max_len, i - left  +1)

        return max_len