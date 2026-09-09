from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-stone for stone in stones]
        heapify(pq)
        while len(pq) > 1:
            s1 = -heappop(pq)
            s2 = -heappop(pq)
            if s1 == s2:
                continue
            heappush(pq, -abs(s1 - s2))
        if pq:
            return -heappop(pq)
        return 0