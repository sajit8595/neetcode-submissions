class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        indeg = [0 for i in range(numCourses)]

        for a, b in prerequisites:
            indeg[a] += 1
            adj[b].append(a)

        dq = deque([])
        for node in range(numCourses):
            if indeg[node] == 0:
                dq.append(node)
        
        topo = []
        while dq:
            node = dq.popleft()
            topo.append(node)
            for child in adj[node]:
                indeg[child] -= 1
                if indeg[child] == 0:
                    dq.append(child)
        
        return len(topo) == numCourses