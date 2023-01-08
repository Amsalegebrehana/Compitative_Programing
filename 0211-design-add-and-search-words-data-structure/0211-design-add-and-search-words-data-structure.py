class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root= TrieNode()    
    
    def addWord(self, word: str) -> None:
        
        currNode = self.root
        
        for ch in word:
            currNode = currNode.children[ch]
            
        currNode.end = True

    def search(self, word: str, currNode = None) -> bool:
        if currNode == None:
            currNode = self.root
        
        for i,ch in enumerate(word):
            if ch == ".":
                for node in currNode.children:
                    if self.search(word[i+1:], currNode.children[node]):   
                        return True
                    
                return False
            
            elif ch not in currNode.children:
                return False
            
            currNode = currNode.children[ch]
            
        return currNode.end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)