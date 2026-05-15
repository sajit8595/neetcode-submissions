from heapq import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        for i in range(k-1):
            heapq.heappush(pq, (-nums[i], i))
        
        ans = []
        for i in range(k-1, len(nums)):
            heapq.heappush(pq, (-nums[i], i))
            ans.append(-pq[0][0])
            while pq and pq[0][1] <= i - k + 1:
                heapq.heappop(pq)
        return ans