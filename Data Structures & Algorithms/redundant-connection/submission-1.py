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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        dsu = DSU(n)

        ans = []
        for a, b in edges:
            if dsu.union(a, b) == False:
                ans = [a, b]
        
        return ans
