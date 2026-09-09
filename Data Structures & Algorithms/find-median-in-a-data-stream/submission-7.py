from heapq import *

class MedianFinder:

    def __init__(self):
        self.maxH = []
        self.minH = []

    def addNum(self, num: int) -> None:
        if not self.maxH or -self.maxH[0] >= num:
            heappush(self.maxH, -num)
        else:
            heappush(self.minH, num)
        self._maintainMaxHLarger()

    def _maintainMaxHLarger(self):
        n1, n2 = len(self.maxH), len(self.minH)
        if n1 == n2 or n1 == n2 + 1:
            return
        
        if n1 > n2 + 1:
            heappush(self.minH, -heappop(self.maxH))
        else:
            heappush(self.maxH, -heappop(self.minH))

    def findMedian(self) -> float:
        if not self.maxH:
            return -1
            
        if len(self.maxH) == len(self.minH):
            m1 = -self.maxH[0]
            m2 = self.minH[0]
            return (m1 + m2) / 2.0

        return -self.maxH[0] / 1.0
        