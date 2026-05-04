class DSU:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]

    def unionBySize(self, u, v):
        uPar = self.find(u)
        vPar = self.find(v)
        if uPar == vPar:
            return False
        if self.size[uPar] >= self.size[vPar]:
            self.size[uPar] += self.size[vPar]
            self.par[vPar] = uPar
        else:
            self.size[vPar] += self.size[uPar]
            self.par[uPar] = vPar
        return True        

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dsu = DSU(n*m)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    u = (row * m) + col
                    for x, y in dirs:
                        nrow, ncol = row+x, col+y
                        if nrow >= 0 and ncol >= 0 and nrow < n and ncol < m and grid[nrow][ncol] == 1:
                            v = (nrow * m) + ncol
                            dsu.unionBySize(u, v)
                    ans = max(ans, dsu.size[dsu.find(u)])
        return ans
        