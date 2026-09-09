from heapq import *

class MedianFinder:

    def __init__(self):
        self.maxH = []
        self.minH = []
        self.n1 = self.n2 = 0

    def addNum(self, num: int) -> None:
        if not self.maxH or -self.maxH[0] >= num:
            heappush(self.maxH, -num)
            self._maintain(self.maxH, self.minH)
        else:
            heappush(self.minH, num)
            self._maintain(self.minH, self.maxH)

    def _maintain(self, h1, h2):
        n1, n2 = len(self.maxH), len(self.minH)
        if n1 == n2 or n1 == n2 + 1:
            return
        heappush(h2, -heappop(h1))

    def findMedian(self) -> float:
        if not self.maxH:
            return -1
            
        if len(self.maxH) == len(self.minH):
            m1 = -self.maxH[0]
            m2 = self.minH[0]
            return (m1 + m2) / 2.0

        return -self.maxH[0] / 1.0
        