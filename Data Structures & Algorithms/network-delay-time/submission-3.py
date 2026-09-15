class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = [[] for i in range(n+1)]
        for u, v, t in times:
            adj[u].append((v, t))
        
        INF = 10**7
        pq = [(0, k)]
        dist = [INF for i in range(n+1)]
        dist[k] = 0

        while pq:
            time, node = heapq.heappop(pq)
            if time > dist[node]:
                continue
            for child, ntime in adj[node]:
                newTime = time + ntime
                if newTime < dist[child]:
                    dist[child] = newTime
                    heapq.heappush(pq, (newTime, child))
        
        dist[0] = 0
        ans = max(dist)
        if ans == INF:
            return -1
        return ans