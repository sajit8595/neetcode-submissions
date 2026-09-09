from heapq import *

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heappush(self.pq, val)
        if len(self.pq) > self.k:
            heappop(self.pq)
        return self.pq[0]



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kthLarge = KthLargest(k, nums)
        return kthLarge.pq[0]