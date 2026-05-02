class Trie:
    def __init__(self):
        self.child = {}
        self.isWordEnd = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = Trie()
            curr = curr.child[ch]
        curr.isWordEnd = True              

    def getEndNode(self, word: str) -> Trie:
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                return None
            curr = curr.child[ch]
        return curr

    def search(self, word: str) -> bool:
        trieNode = self.getEndNode(word)
        return trieNode.isWordEnd if trieNode else False

    def startsWith(self, prefix: str) -> bool:
        trieNode = self.getEndNode(prefix)
        return True if trieNode else False

