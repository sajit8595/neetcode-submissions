class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        memo = {}

        def recur(i, j):
            if j < 0:
                return 1
            if i < 0:
                return 0
            key = (i, j)
            if key in memo:
                return memo[key]
            ntake = recur(i-1, j)
            take = 0
            if s[i] == t[j]:
                take = recur(i-1, j-1)
            memo[key] = take + ntake
            return memo[key]
        
        n, m = len(s), len(t)
        return recur(n-1, m-1)