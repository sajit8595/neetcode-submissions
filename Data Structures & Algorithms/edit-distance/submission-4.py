class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        memo = {}
        def recur(i, j):
            if j == m:
                return n - i
            if i == n:
                return m - j
            
            key = (i, j)
            if key in memo:
                return memo[key]

            if word1[i] == word2[j]:
                memo[key] = recur(i+1, j+1)
            else:
                replace = recur(i+1, j+1)
                delete = recur(i+1, j)
                insert = recur(i, j+1)
                memo[key] = 1 + min(replace, delete, insert)

            return memo[key]
        
        return recur(0, 0)