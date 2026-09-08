class Node:
    def __init__(self):
        self.child = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = Node()
            curr = curr.child[w]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        return self.search_2(0, word, self.root)

    def search_ind(self, ind, word, curr):
        for child in curr.child:
            if (self.search_2(ind+1, word, curr.child[child])):
                return True
        return False
    
    def search_2(self, ind, word, curr):
        n = len(word)
        for i in range(ind, n):
            w = word[i]
            if w == '.':
                return self.search_ind(i, word, curr)
            if w not in curr.child:
                return False
            curr = curr.child[w]
        return curr.isEnd

class WordDictionary:

    def __init__(self):
        self.pt = PrefixTree()
        
    def addWord(self, word: str) -> None:
        self.pt.insert(word)

    def search(self, word: str) -> bool:
        return self.pt.search(word)
        
