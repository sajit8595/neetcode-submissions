class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        x, y = points[0]
        pq = [(0, x, y)]
        vis = set()

        ans = 0
        while pq:
            w, x, y = heapq.heappop(pq)
            if (x, y) in vis:
                continue

            vis.add((x, y))
            ans += w

            for nx, ny in points:
                if (nx, ny) not in vis:
                    nw = abs(x - nx) + abs(y - ny)
                    heapq.heappush(pq, (nw, nx, ny))
        
        return ans