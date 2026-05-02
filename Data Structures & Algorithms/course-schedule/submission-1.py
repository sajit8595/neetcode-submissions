from collections import deque

class Solution:
    def canFinish(self, n: int, prereq: List[List[int]]) -> bool:
        adj = {}

        indeg = [0] * n
        for a, b in prereq:
            indeg[a] += 1
            if b not in adj:
                adj[b] = []
            adj[b].append(a)
        
        dq = deque([])
        for i in range(n):
            if indeg[i] == 0:
                dq.append(i)
        
        topo = []
        while dq:
            node = dq.popleft()
            topo.append(node)
            if node in adj:
                for child in adj[node]:
                    indeg[child] -= 1
                    if indeg[child] == 0:
                        dq.append(child)
                
        return len(topo) == n
