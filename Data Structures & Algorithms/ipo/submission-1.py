import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        pc = [(-profits[i], capital[i]) for i in range(n)]

        heapq.heapify(pc)
        while k > 0 and pc:
            future = []
            while pc:
                p, c = heapq.heappop(pc)
                if c <= w:
                    w += (-p)
                    k -= 1
                    while future:
                        heapq.heappush(pc, future.pop())
                    break
                else:
                    future.append((p, c))
        return w