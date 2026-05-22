class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def check(val, level):
            return val <= level

        n, m = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        pq = []
        vis = set()

        heapq.heappush(pq, (grid[0][0], 0, 0))
        vis.add((0, 0))

        while pq:
            pqLen = len(pq)
            for ele in range(pqLen):
                lvl, i, j = heapq.heappop(pq)
                if i == n-1 and j == m-1:
                    return lvl

                for di, dj in dirs:
                    ni, nj = i+di, j+dj
                    if ni >= 0 and nj >= 0 and ni < n and nj < m and (ni, nj) not in vis:
                        nlvl = max(grid[ni][nj], lvl)
                        heapq.heappush(pq, (nlvl, ni, nj))
                        vis.add((ni, nj))
        return -1
                
