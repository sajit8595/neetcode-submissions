from heapq import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []

        ans = []
        for i in range(len(nums)):
            heapq.heappush(pq, (-nums[i], i))
            if i >= k-1:
                ans.append(-pq[0][0])
                while pq and pq[0][1] <= i - k + 1:
                    heapq.heappop(pq)
        return ans