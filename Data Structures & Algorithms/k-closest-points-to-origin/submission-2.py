from heapq import *

class KthLargest:
    def __init__(self, k: int) -> None:
        self.pq = []
        self.k = k

    def add(self, val) -> None:
        heappush(self.pq, val)
        if len(self.pq) > self.k:
            heappop(self.pq)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kClose = KthLargest(k)
        for p in points:
            kClose.add((-(p[0]**2 + p[1]**2), p))
        return [x[1] for x in kClose.pq]