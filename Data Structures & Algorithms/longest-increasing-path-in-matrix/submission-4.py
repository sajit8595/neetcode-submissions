class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
            
        n, m = len(mat), len(mat[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        dp = [[1] * m for _ in range(n)]
        
        cells = []
        for i in range(n):
            for j in range(m):
                cells.append((i, j))
                
        cells.sort(key=lambda x: mat[x[0]][x[1]], reverse=True)
        
        ans = 0
        for i, j in cells:
            for xi, yi in dirs:
                ni, nj = i + xi, j + yi
                if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] > mat[i][j]:
                    dp[i][j] = max(dp[i][j], 1 + dp[ni][nj])
            
            ans = max(ans, dp[i][j])
            
        return ans