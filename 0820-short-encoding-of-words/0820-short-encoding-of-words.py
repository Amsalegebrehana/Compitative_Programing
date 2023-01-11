class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        w = set(words)
        for word in words:
            for j in range(1,len(word)):
                if word[j:] in w:
                    w.remove(word[j:])

        return len("#".join(w)) + 1
                    