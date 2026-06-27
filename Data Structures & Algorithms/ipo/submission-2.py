import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        pc = [(-profits[i], capital[i]) for i in range(n)]
        cp = []
        heapq.heapify(pc)

        while k > 0 and pc:
            while pc:
                p, c = heapq.heappop(pc)
                if c <= w:
                    w += (-p)
                    k -= 1
                    while cp and cp[0][0] <= w:
                        c, p = heapq.heappop(cp)
                        heapq.heappush(pc, (p, c))
                    break
                else:
                    heapq.heappush(cp, (c, p))
        return w