class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n, m = len(board), len(board[0])

        notSurrounded = set()

        def dfs(i, j):
            notSurrounded.add((i, j))
            for x, y in dirs:
                ni, nj = i+x, j+y
                if ni >= 0 and nj >= 0 and ni < n and nj < m and board[ni][nj] == 'O':
                    if ((ni, nj) not in notSurrounded):
                        dfs(ni, nj)
        
        for i in range(n):
            if board[i][0] == 'O' and (i, 0) not in notSurrounded:
                dfs(i, 0)
            if board[i][m-1] == 'O' and (i, m-1) not in notSurrounded:
                dfs(i, m-1)
        
        for j in range(m):
            if board[0][j] == 'O' and (0, j) not in notSurrounded:
                dfs(0, j)
            if board[n-1][j] == 'O' and (n-1, j) not in notSurrounded:
                dfs(n-1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i, j) not in notSurrounded:
                    board[i][j] = 'X'
        
        
