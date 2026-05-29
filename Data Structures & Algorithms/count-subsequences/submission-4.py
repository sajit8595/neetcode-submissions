class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        dp = [0 for j in range(m+1)]
        j = 0
        dp[j] = 1

        for i in range(1, n+1):
            ndp = [0 for j in range(m+1)]
            j = 0
            ndp[j] = 1

            for j in range(1, m+1):
                ntake = dp[j]
                take = 0
                if s[i-1] == t[j-1]:
                    take = dp[j-1]
                ndp[j] = take + ntake
            dp = ndp
        return dp[m]