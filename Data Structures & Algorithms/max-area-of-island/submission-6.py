class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        vis = [[False for j in range(n)] for i in range(m)]

        def dfs(i, j):
            vis[i][j] = True
            area = 1
            for x, y in dirs:
                ni, nj = x+i, y+j
                if ni >= 0 and nj >= 0 and ni < m and nj < n and vis[ni][nj] == False and grid[ni][nj] == 1:
                    area += dfs(ni, nj)
            return area

        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and vis[i][j] == False:
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)
        return maxArea
