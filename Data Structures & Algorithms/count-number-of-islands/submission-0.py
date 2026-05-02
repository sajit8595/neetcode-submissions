class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = "#"
            for x, y in dirs:
                ni, nj = i+x, j+y
                if ni >= 0 and nj >= 0 and ni < n and nj < m and grid[ni][nj] == "1":
                    dfs(ni, nj)

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "#":
                    grid[i][j] = "1"
        return ans