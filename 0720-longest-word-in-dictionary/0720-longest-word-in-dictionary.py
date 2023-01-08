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
        
    def validate(self, word):
        currNode = self.root
        
        for ch in word:
            currNode = currNode.children[ch]
            if not currNode.end :
                return False
            
        return True
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        currword = ""
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        for word in words:
            if trie.validate(word):
                
                if (len(currword) < len(word)) or \
                    (len(currword) == len(word) and currword > word):
                    currword = word
                            
        return  currword
                        
            
            
        
        
        
        
        
        