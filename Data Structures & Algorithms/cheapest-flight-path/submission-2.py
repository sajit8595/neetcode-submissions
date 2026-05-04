from heapq import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for i in range(n)]
        for u, v, p in flights:
            adj[u].append((v, p))

        money = [float('inf') for i in range(n)]
        money[src] = 0
        pq = [(-1, 0, src)]
        while pq:
            print(pq)
            kth, mon, node = heappop(pq)
            if kth == k:
                continue
            for child, price in adj[node]:
                print(child)
                newMoney = mon + price
                if newMoney < money[child]:
                    money[child] = newMoney
                    heappush(pq, (kth+1, newMoney, child))
        
        if money[dst] == float('inf'):
            return -1
        return money[dst] 
        