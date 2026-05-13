class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dq = deque([])
        n = len(beginWord)
        dq.append((beginWord, 1))

        wordSet = set(wordList)

        while dq:
            word, ans = dq.popleft()
            if word == endWord:
                return ans
            
            for ind in range(n):
                for char in 'abcdefghikjlmnopqrstuvwxyz':
                    if char != word[ind]:
                        newWord = word[:ind] + char + word[ind+1:]
                        if newWord in wordSet:
                            dq.append((newWord, ans + 1))
                            wordSet.remove(newWord)
    
        return 0

        # missing - focus on question, dont miss edge case,
        # no.of words instead of no.of steps && return empty base
        # updating of map