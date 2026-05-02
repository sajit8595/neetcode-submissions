class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        n1, n2 = len(t1), len(t2)

        def recursion(i, j):
            if i == 0 and j == 0:
                return 1 if t1[i] == t2[j] else 0
            if i == 0:
                for nj in range(j, -1, -1):
                    if t1[i] == t2[nj]:
                        return 1
                return 0
            if j == 0:
                for ni in range(i, -1, -1):
                    if t1[ni] == t2[j]:
                        return 1
                return 0
            if t1[i] == t2[j]:
                return 1 + recursion(i-1, j-1)
            a = recursion(i-1, j)
            b = recursion(i, j-1)
            return max(a, b)

        # return recursion(n1-1, n2-1)

        dp = [[0 for j in range(n2+1)] for i in range(n1+1)]
        # i = 0
        # for j in range(n2-1, -1, -1):
        #     if t1[i] == t2[j]:
        #         dp[i][j] = 1
        # j = 0
        # for i in range(n1-1, -1, -1):
        #     if t1[i] == t2[j]:
        #         dp[i][j] = 1

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if t1[i-1] == t2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n1][n2]