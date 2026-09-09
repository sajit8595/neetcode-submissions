class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = [[] for i in range(n+1)]
        for u, v, t in times:
            adj[u].append((v, t))
        
        INF = 10**7
        dq = deque([(k, 0)])
        dist = [INF for i in range(n+1)]
        dist[0] = dist[k] = 0
        
        while dq:
            node, time = dq.popleft()
            for child, ntime in adj[node]:
                if dist[child] > time + ntime:
                    dist[child] = time + ntime
                    dq.append((child, time + ntime))
        
        ans = max(dist)
        if ans == INF:
            return -1
        return ans