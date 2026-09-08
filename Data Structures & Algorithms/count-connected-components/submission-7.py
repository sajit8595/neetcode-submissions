class DSU:
    def __init__(self, n):
        self.size = [1 for i in range(n)]
        self.par = [i for i in range(n)]
    
    def union(self, u, v):
        up, vp = self.findPar(u), self.findPar(v)
        if up == vp:
            return False
        if self.size[up] >= self.size[vp]:
            self.size[up] += self.size[vp]
            self.par[vp] = up
        else:
            self.size[vp] += self.size[up]
            self.par[up] = vp

        return True
    
    def findPar(self, u):
        if self.par[u] != u:
            self.par[u] = self.findPar(self.par[u])
        return self.par[u]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for a, b in edges:
            dsu.union(a, b)
        
        count = 0
        for i in range(n):
            if i == dsu.findPar(i):
                count += 1

        return count