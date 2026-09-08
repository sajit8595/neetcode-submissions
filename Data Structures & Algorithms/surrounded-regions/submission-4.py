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
        

        def performDfs(i, j):
            if board[i][j] == 'O' and (i, j) not in notSurrounded:
                dfs(i, j)

        for i in range(n):
            performDfs(i, 0)
            performDfs(i, m-1)
        
        for j in range(m):
            performDfs(0, j)
            performDfs(n-1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i, j) not in notSurrounded:
                    board[i][j] = 'X'
        
        
