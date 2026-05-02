class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # no blockers - proper math
        # but dp in mind
        
        def recursion(i, j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            down = recursion(i+1, j)
            right = recursion(i, j+1)
            return down + right
            
        # return recursion(0, 0)

        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                down = dp[i+1][j]
                right = dp[i][j+1]
                dp[i][j] += (down + right)
        return dp[0][0]