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

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
        return curr.isWordEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
        return True

