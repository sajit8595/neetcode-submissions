from heapq import *

class MedianFinder:
    # 1 to mid1 - last ele - maxHeap
    # mid1+1 to n - first ele - minHeap
    def __init__(self):
        self.maxHeap = []
        self.n1 = 0
        self.minHeap = []
        self.n2 = 0

    def maintain_n1_large(self):
        if self.n1 == self.n2 or self.n1 - 1 == self.n2:
            return
        if self.n1 > self.n2:
            pop = heappop(self.maxHeap)
            heappush(self.minHeap, -pop)
            self.n1 -= 1
            self.n2 += 1
        elif self.n1 < self.n2:
            pop = heappop(self.minHeap)
            heappush(self.maxHeap, -pop)
            self.n2 -= 1
            self.n1 += 1

    def addNum(self, num: int) -> None:            
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
            self.n1 += 1
        else:
            heappush(self.minHeap, num)
            self.n2 += 1
        self.maintain_n1_large()

    def findMedian(self) -> float:
        if self.n1 == self.n2:
            return (-self.maxHeap[0]+self.minHeap[0]) / 2.0
        return -self.maxHeap[0] / 1.0
        