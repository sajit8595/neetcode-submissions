class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def diagonalCheck(i, j, board, di, dj):
            while i >= 0 and j >= 0 and i < n and j < n:
                if board[i][j] == 'Q':
                    return False
                i += di
                j += dj
            return True

        def isValid(r, c, board):
            for i in range(n):
                if board[r][i] == 'Q' or board[i][c] == 'Q':
                    return False
            
            return\
            diagonalCheck(r, c, board, 1, 1) and\
            diagonalCheck(r, c, board, -1, -1) and\
            diagonalCheck(r, c, board, -1, 1) and\
            diagonalCheck(r, c, board, 1, -1)
    
        def backtrack(row, board):
            if row >= n:
                ans.append([''.join(b) for b in board])
                return
            
            for col in range(n):
                if isValid(row, col, board):
                    board[row][col] = 'Q'
                    backtrack(row + 1, board)
                    board[row][col] = '.'
        
        ans = []
        board = [['.' for j in range(n)] for i in range(n)]
        backtrack(0, board)
        return ans
