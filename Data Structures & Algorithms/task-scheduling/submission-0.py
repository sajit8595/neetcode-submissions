class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        pq = []
        for key in freq:
            pq.append(-freq[key])
        
        heapq.heapify(pq)

        time = 0
        while pq:
            newPq = []
            pqn = min(len(pq), n+1)
            for i in range(pqn):
                mostFreq = -heapq.heappop(pq)
                mostFreq -= 1
                if mostFreq > 0:
                    newPq.append(mostFreq)
                time += 1
            
            # I have to idleWait for new childs.. and time wait = total - consumed
            # total = n+1, consumed = min(len(pq), n+1)
            if newPq:
                time += (n + 1 - pqn)

            for new in newPq:
                heapq.heappush(pq, -new)
        
        return time
            