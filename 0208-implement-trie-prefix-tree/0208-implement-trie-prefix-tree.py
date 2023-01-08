class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        
        for w in word:
            currNode = currNode.children[w]
            
        currNode.end = True
        
    def search(self, word: str) -> bool:
        return self.startsWith(word, isPre=False)
        
    def startsWith(self, prefix: str, isPre=True) -> bool:
        currNode = self.root
        
        for ch in prefix:
            if ch not in currNode.children:
                return False
            currNode = currNode.children[ch]
            
        return currNode.end or isPre

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)