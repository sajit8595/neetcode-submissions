class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        # memo = {}
        # def recur(i, j):
        #     if j == m:
        #         return n - i
        #     if i == n:
        #         return m - j
            
        #     key = (i, j)
        #     if key in memo:
        #         return memo[key]

        #     if word1[i] == word2[j]:
        #         memo[key] = recur(i+1, j+1)
        #     else:
        #         replace = recur(i+1, j+1)
        #         delete = recur(i+1, j)
        #         insert = recur(i, j+1)
        #         memo[key] = 1 + min(replace, delete, insert)

        #     return memo[key]
        
        # return recur(0, 0)

        dp = [float('inf') for j in range(m+1)]
        # j = m
        # for i in range(n+1):
        #     dp[j] = n - i
        # i = n
        for j in range(m+1):
            dp[j] = m - j
        
        for i in range(n-1, -1, -1):
            ndp = [float('inf') for j in range(m+1)]
            ndp[m] = n - i
            for j in range(m-1, -1, -1):
                if word1[i] == word2[j]:
                    ndp[j] = dp[j+1]
                else:
                    replace = dp[j+1]
                    delete = dp[j]
                    insert = ndp[j+1]
                    ndp[j] = 1 + min(replace, delete, insert)
            dp = ndp

        return dp[0]
