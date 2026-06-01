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
            self.size[uPar] += 1
            self.par[vPar] = uPar
        else:
            self.size[vPar] += 1
            self.par[uPar] = vPar
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.unionBySize(u, v)
        for i in range(n):
            dsu.find(i)
        return len(set(dsu.par))
        