class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        wordLen = len(beginWord)

        dq = deque([])
        vis = set()

        dq.append(beginWord)
        vis.add(beginWord)

        lvl = 1
        while dq:
            for _ in range(len(dq)):
                currWord = dq.popleft()
                if currWord == endWord:
                    return lvl
                for i in range(wordLen):
                    for c in range(26):
                        ch = chr(ord('a') + c)
                        if ch == currWord[i]:
                            continue
                        newWord = currWord[:i] + ch + currWord[i+1:]
                        if newWord not in vis and newWord in wordSet:
                            dq.append(newWord)
                            vis.add(newWord)
            lvl += 1
        
        return 0

