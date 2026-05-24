class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        memo = {}
        def recur(i, j):
            key = (i, j)
            if key in memo:
                return memo[key]

            ans = 1
            for xi, yi in dirs:
                ni, nj = i + xi, j + yi
                if ni >= 0 and nj >= 0 and ni < n and nj < m and mat[ni][nj] > mat[i][j]:
                    ans = max(ans, 1 + recur(ni, nj))
            memo[key] = ans
            return memo[key]

        dp = [[0 for j in range(m)] for i in range(n)]

        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, recur(i, j))
        return ans
        