class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        n = len(pref)
        for word in words:
            if pref == word[:n]:
                result +=1
        return result
            