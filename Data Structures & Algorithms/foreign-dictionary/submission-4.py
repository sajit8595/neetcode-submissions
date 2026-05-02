from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        def getTopoSort(adj):
            indeg = {c: 0 for c in adj}
            for a in adj:
                for b in adj[a]:
                    indeg[b] += 1
            
            dq = deque([])
            for key in indeg:
                if indeg[key] == 0:
                    dq.append(key)
                
            topo = []
            while dq:
                node = dq.popleft()
                topo.append(node)
                if node in adj:
                    for child in adj[node]:
                        indeg[child] -= 1
                        if indeg[child] == 0:
                            dq.append(child)

            return topo if len(topo) == len(indeg) else []

        adj = {}
        for w in words:
            for c in w:
                adj[c] = []
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            n = min(len(w1), len(w2))
            c = 0
            # IMPO - illegal order, length wise w1 greater, but w2 == w1, then order must be w2, w1
            if len(w1) > len(w2) and w1[:n] == w2[:n]:
                return ""
            while c < n:
                if w1[c] != w2[c]:
                    adj[w1[c]].append(w2[c])
                    break
                c += 1
        topo = getTopoSort(adj)
        return ''.join(topo)