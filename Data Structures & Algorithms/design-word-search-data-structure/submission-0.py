class Trie:
    def __init__(self):
        self.child = {}
        self.isWordEnd = False

class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = Trie()
            curr = curr.child[ch]
        curr.isWordEnd = True
    
    def find(self, curr, word, start) -> bool:
        for i in range(start, len(word)):
            if word[i] != '.':
                if word[i] not in curr.child:
                    return False
                curr = curr.child[word[i]]
            else:
                for ch in curr.child:
                    ans = self.find(curr.child[ch], word, i+1)
                    if ans:
                        return True
                return False
        return curr.isWordEnd


    def search(self, word: str) -> bool:
        return self.find(self.root, word, 0)
