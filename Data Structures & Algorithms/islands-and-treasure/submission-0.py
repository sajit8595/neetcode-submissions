class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        n, m = len(grid), len(grid[0])

        def dfs(i, j, dist):
            for x, y in dirs:
                ni, nj = i+x, j+y
                if ni >= 0 and nj >= 0 and ni < n and nj < m and grid[ni][nj] > 0:
                    newDist = dist + 1
                    if grid[ni][nj] > newDist:
                        grid[ni][nj] = newDist
                        dfs(ni, nj, newDist)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i, j, 0)
        