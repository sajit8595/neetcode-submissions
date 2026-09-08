class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dq = deque([])
        n, m = len(heights), len(heights[0])

        def getVis(dq):
            vis = [[0 for j in range(m)] for i in range(n)]
            for a, b in dq:
                vis[a][b] = 1

            while dq:
                i, j = dq.popleft()
                for x, y in dirs:
                    ni, nj = i+x, j+y
                    if ni >= 0 and nj >= 0 and ni < n and nj < m and vis[ni][nj] == 0:
                        if heights[i][j] <= heights[ni][nj]:
                            vis[ni][nj] = 1
                            dq.append((ni, nj))
                        
            return vis

        pacificDq = deque([])
        atlanticDq = deque([])
        for i in range(n):
            pacificDq.append((i, 0))
            atlanticDq.append((i, m-1))
        for j in range(m):
            pacificDq.append((0, j))
            atlanticDq.append((n-1, j))
        
        pacificVis = getVis(pacificDq)
        atlanticVis = getVis(atlanticDq)

        ans = []
        for i in range(n):
            for j in range(m):
                if pacificVis[i][j] == 1 and atlanticVis[i][j] == 1:
                    ans.append((i, j))
        
        return ans
        
