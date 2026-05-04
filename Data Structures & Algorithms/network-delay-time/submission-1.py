from heapq import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        for u, v, t in times:
            adj[u].append((v, t))
        
        dist = [float('inf') for i in range(n+1)]
        pq = [(0, k)]
        dist[k] = 0
        # vis = set()
        while pq:
            currTime, node = heappop(pq)
            # if currTime > dist[node]:
            #     continue
            for child, time in adj[node]:
                newTime = currTime + time
                if newTime < dist[child]:
                    dist[child] = newTime
                    heappush(pq, (dist[child], child))
        
        ans = 0
        for i in range(1, n+1):
            if dist[i] == float('inf'):
                return -1
            ans = max(ans, dist[i])
        return ans
