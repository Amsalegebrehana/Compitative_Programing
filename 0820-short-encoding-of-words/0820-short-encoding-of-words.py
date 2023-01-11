class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        length = 0
        currNode = self.root
        for ch in word:
            if ch not in currNode.children:
                currNode.children[ch] = TrieNode()
            currNode = currNode.children[ch]
            length+=1
        currNode.end = True
        return length+1
    def startWith(self, word):
        currNode = self.root
        for ch in word:
            if ch not in currNode.children:
                return False
            currNode = currNode.children[ch]
        return True
        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x : len(x), reverse= True)

        trie = Trie()
        encodelen = 0
        for word in words:
            word_reversed = word[::-1]
         
            if not trie.startWith(word_reversed):
                encodelen += trie.insert(word_reversed)
        return encodelen
        