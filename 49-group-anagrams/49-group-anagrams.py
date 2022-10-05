class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            temp = "".join(sorted(i))
            result[temp].append(i)
        return result.values()