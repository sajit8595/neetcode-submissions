class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indeg = [0 for i in range(numCourses)]

        for a, b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1
        
        dq = deque([])
        for i in range(numCourses):
            if indeg[i] == 0:
                dq.append(i)

        topo = []
        while dq:
            node = dq.popleft()
            topo.append(node)
            for child in adj[node]:
                indeg[child] -= 1
                if indeg[child] == 0:
                    dq.append(child)
        
        if len(topo) == numCourses:
            return topo
        return []
                