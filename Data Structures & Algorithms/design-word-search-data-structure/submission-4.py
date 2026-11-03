class Trie:
    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = Trie()
            curr = curr.child[w]
        curr.end = True

    def search(self, word: str) -> bool:
        return self._search2(word, self.root)
    
    def _search2(self, word, curr):
        for i, w in enumerate(word):
            if w == '.':
                for child in curr.child:
                    searchNext = self._search2(word[i+1:], curr.child[child])
                    if searchNext:
                        return True
                return False
            else:
                if w not in curr.child:
                    return False
                curr = curr.child[w]
        return curr.end
