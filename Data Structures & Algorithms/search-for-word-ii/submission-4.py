class Trie:
    def __init__(self):
        self.child = {}
        self.isWordEnd = False
    
class PrefixTrie:
    def __init__(self):
        self.root = Trie()
    
    def addWord(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = Trie()
            curr = curr.child[ch]
        curr.isWordEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])

        trie = PrefixTrie()
        for word in words:
            trie.addWord(word)
        
        ans = set()
        vis = set()

        def dfs(i, j, root, word):
            ch = board[i][j]
            if ch not in root.child:
                return

            vis.add((i, j))
            root = root.child[ch]
            word += ch
            if root.isWordEnd:
                ans.add(word)
            
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i+x, j+y
                if ni >= 0 and nj >= 0 and ni < n and nj < m and (ni, nj) not in vis:
                    dfs(ni, nj, root, word)
            
            vis.remove((i, j))

        for i in range(n):
            for j in range(m):
                dfs(i, j, trie.root, "")

        return list(ans)
        