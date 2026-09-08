class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dq = deque([])
        n, m = len(grid), len(grid[0])

        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    dq.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        time = 0
        while dq and fresh:
            for _ in range(len(dq)):
                i, j = dq.popleft()
                for x, y in dirs:
                    ni, nj = i+x, j+y
                    if ni >= 0 and nj >= 0 and ni < n and nj < m and grid[ni][nj] == 1:
                        fresh -= 1
                        grid[ni][nj] = 2
                        dq.append((ni, nj))
            time += 1
            
        return time if fresh == 0 else -1