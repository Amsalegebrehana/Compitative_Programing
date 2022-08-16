class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = Node()
            curr = curr.children[index] 
        curr.end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            index =  ord(ch) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index] 
            
        return curr.end
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            index =  ord(ch) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index] 
            
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)