
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for i in range(n)]
        for u, v, p in flights:
            adj[u].append((v, p))

        money = [float('inf') for i in range(n)]
        money[src] = 0
        dq = deque([(0, 0, src)])
        while dq:
            kth, mon, node = dq.popleft()
            if kth > k:
                continue
            for child, price in adj[node]:
                newMoney = mon + price
                if newMoney < money[child]:
                    money[child] = newMoney
                    dq.append((kth+1, newMoney, child))
        
        if money[dst] == float('inf'):
            return -1
        return money[dst] 
        