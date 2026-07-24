class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # * means, zero or more preceding element

        n, m = len(s), len(p)
        def recur(i, j):
            if j == m:
                return i == n

            match = False
            if i < n:
                match = (s[i] == p[j]) or (p[j] == '.')

            if j+1 < m and p[j+1] == '*':
                zero = recur(i, j+2)
                oneOrMore = False
                if match:
                    oneOrMore = recur(i+1, j)
                return zero or oneOrMore
            
            return match and recur(i+1, j+1)
        
        # return recur(0, 0)
        dp = [[False for j in range(m+2)] for i in range(n+1)]

        dp[n][m] = True
        for i in range(n, -1, -1):
            for j in range(m-1, -1, -1):
                match = False
                if i < n:
                    match = (s[i] == p[j]) or (p[j] == '.')

                if j+1 < m and p[j+1] == '*':
                    zero = dp[i][j+2]
                    oneOrMore = False
                    if match:
                        oneOrMore = dp[i+1][j]
                    dp[i][j] = zero or oneOrMore
                else:
                    dp[i][j] = match and dp[i+1][j+1]

        # print(dp)
        return dp[0][0]