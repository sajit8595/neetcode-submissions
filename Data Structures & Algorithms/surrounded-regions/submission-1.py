class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        n, m = len(board), len(board[0])

        def dfs(i, j):
            board[i][j] = 'A';
            for x, y in dirs:
                ni, nj = i+x, j+y
                if ni >= 0 and nj >= 0 and ni < n and nj < m and board[ni][nj] == 'O':
                    dfs(ni, nj)
                    
        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m-1] == 'O':
                dfs(i, m-1)
        for i in range(m):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[n-1][i] == 'O':
                dfs(n-1, i)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O';
        
