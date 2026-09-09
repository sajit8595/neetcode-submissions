from heapq import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = {}
        for t in tasks:
            mp[t] = mp.get(t, 0) - 1
        
        pq = list(mp.values())
        heapify(pq)

        time = 0
        while pq:
            minTime = min(n+1, len(pq))
            remTime = n + 1 - minTime
            time += minTime
            npq = []
            for _ in range(minTime):
                x = -heappop(pq) - 1
                if x > 0: npq.append(x)

            if npq: time += remTime
            while npq: heappush(pq, -npq.pop())
        return time
            