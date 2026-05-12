class DSU:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def findPar(self, node):
        parNode = self.par[node]
        if parNode == node:
            return node
        self.par[node] = self.findPar(parNode)
        return self.par[node]
    
    def union(self, a, b):
        aPar = self.findPar(a)
        bPar = self.findPar(b)
        if aPar == bPar:
            return False
        if self.size[aPar] >= self.size[bPar]:
            self.size[aPar] += self.size[bPar]
            self.par[bPar] = aPar
        else:
            self.size[bPar] += self.size[aPar]
            self.par[aPar] = bPar
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n+1)

        for i in range(n):
            u, v = edges[i]
            if dsu.union(u, v) == False:
                return edges[i]
        return []
            



        