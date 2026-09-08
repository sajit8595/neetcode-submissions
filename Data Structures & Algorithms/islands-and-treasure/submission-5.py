from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        INF = (2 ** 31) - 1
        n, m = len(grid), len(grid[0])

        dq = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dq.append((i, j))        

        while dq:
            i, j = dq.popleft()
            for x, y in dirs:
                ni, nj = x+i, y+j
                if ni >= 0 and nj >= 0 and ni < n and nj < m and grid[ni][nj] == INF:
                    if grid[ni][nj] > grid[i][j]:
                        grid[ni][nj] = 1 + grid[i][j]
                        dq.append((ni, nj))