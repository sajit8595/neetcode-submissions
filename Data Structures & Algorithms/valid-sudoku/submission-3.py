class Solution:
    def isValidSudoku(self, board):
        # row check
        for row in range(9):
            visRow = set()
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in visRow:
                    return False
                visRow.add(board[row][col])
        
        # col check
        for row in range(9):
            visCol = set()
            for col in range(9):
                if board[col][row] == '.':
                    continue
                if board[col][row] in visCol:
                    return False
                visCol.add(board[col][row])
                
        # square check
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                visSquare = set()
                for sr in range(row, row+3):
                    for sc in range(col, col+3):
                        if board[sr][sc] == '.':
                            continue
                        if board[sr][sc] in visSquare:
                            return False
                        visSquare.add(board[sr][sc])
        return True
