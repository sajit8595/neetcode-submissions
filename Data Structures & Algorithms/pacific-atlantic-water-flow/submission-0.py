class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        pacific = [[0 for j in range(m)] for i in range(n)]
        atlantic  = [[0 for j in range(m)] for i in range(n)]

        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(i, j, mat):
            mat[i][j] = 1
            for x, y in dirs:
                ni, nj = i+x, j+y
                if ni >= 0 and nj >= 0 and ni < n and nj < m and mat[ni][nj] == 0 and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, mat)
        
        for i in range(n):
            dfs(i, 0, pacific)
            dfs(i, m-1, atlantic)

        for j in range(m):
            dfs(0, j, pacific)
            dfs(n-1, j, atlantic)

        ans = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    ans.append((i, j))
        return ans
