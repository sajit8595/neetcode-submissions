class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ns = len(word)
        n, m = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def search(i, j, ind):
            if ind == ns:
                return True
            
            if i < 0 or j < 0 or i >= n or j >= m or board[i][j] == '#' or board[i][j] != word[ind]:
                return False

            board[i][j] = '#'
            for x, y in dirs:
                if search(i+x, j+y, ind+1):
                    return True
            board[i][j] = word[ind]
            return False
        
        for i in range(n):
            for j in range(m):
                if search(i, j, 0):
                    return True
        return False