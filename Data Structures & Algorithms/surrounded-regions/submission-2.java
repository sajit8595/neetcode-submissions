
class Solution {
    int[][] dirs = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    int n; int m;

    public void dfs(int i, int j, char[][] board) {
        board[i][j] = 'A';
        for (int ind = 0; ind < 4; ind++) {
            int newI = i + dirs[ind][0];
            int newJ = j + dirs[ind][1];
            if (newI >= 0 && newJ >= 0 
            && newI < board.length && newJ < board[0].length 
            && board[newI][newJ] == 'O') {
                dfs(newI, newJ, board);
            }
        }
    }

    public void solve(char[][] board) {
        int n = board.length;
        int m = board[0].length;

        for (int i = 0; i < n; i++) {
            if (board[i][0] == 'O') {
                dfs(i, 0, board);
            }
            if (board[i][m-1] == 'O') {
                dfs(i, m-1, board);
            }
        }

        for (int j = 0; j < m; j++) {
            if (board[0][j] == 'O') {
                dfs(0, j, board);
            }
            if (board[n-1][j] == 'O') {
                dfs(n-1, j, board);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j ++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if (board[i][j] == 'A') {
                    board[i][j] = 'O';
                }
            }
        }
        
    }
}
