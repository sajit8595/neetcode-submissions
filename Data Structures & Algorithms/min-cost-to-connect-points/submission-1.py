from heapq import *

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prism's algo
        # select edges with less weight

        pq = []
        vis = set()

        x, y = points[0]
        pq.append([0, x, y])

        ans = 0

        while pq:
            val, x, y = heappop(pq)
            # this point is already recorded, with lowest distance
            if (x, y) in vis:
                continue
            
            ans += val
            vis.add((x, y))

            for nx, ny in points:
                if (nx, ny) not in vis:
                    nval = abs(x - nx) + abs(y - ny)
                    heappush(pq, (nval, nx, ny))
        
        return ans
            

            