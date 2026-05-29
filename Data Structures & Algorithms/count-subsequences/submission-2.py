class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        dp = [[0 for j in range(m+1)] for i in range(n+1)]

        j = 0
        for i in range(n+1):
            dp[i][j] = 1
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                ntake = dp[i-1][j]
                take = 0
                if s[i-1] == t[j-1]:
                    take = dp[i-1][j-1]
                dp[i][j] = take + ntake
        
        return dp[n][m]