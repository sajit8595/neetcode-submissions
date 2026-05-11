class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heaps = [[(x**2) + (y**2), x, y] for x, y in points]
        heapq.heapify(heaps)
        ans = []
        while k:
            dist, x, y = heapq.heappop(heaps)
            ans.append([x, y])
            k -= 1
        return ans
