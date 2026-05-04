class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dq = deque([])
        allFresh = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    dq.append((r, c))
                elif grid[r][c] == 1:
                    allFresh += 1

        time = 0
        while dq:
            if allFresh == 0:
                return time
            for i in range(len(dq)):
                r, c = dq.popleft()
                for x, y in dirs:
                    nr, nc = r+x, c+y
                    if nr >= 0 and nc >= 0 and nr < n and nc < m and grid[nr][nc] == 1:
                        allFresh -= 1
                        dq.append((nr, nc))
                        grid[nr][nc] = 2
            time += 1
        if allFresh > 0:
            return -1
        return time