from heapq import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        mp = {}
        for t in tasks:
            if t not in mp:
                mp[t] = 0
            mp[t] += 1
        
        for t in mp:
            pq.append(-mp[t])
        
        heapify(pq)

        time = 0
        while pq:
            npq = []
            minTime = min(n+1, len(pq))
            remTime = n + 1 - minTime
            time += minTime
            for _ in range(minTime):
                x = -heappop(pq) - 1
                if x > 0:
                    npq.append(x)

            if npq:
                time += remTime
                while npq:
                    heappush(pq, -npq.pop())
        return time
            