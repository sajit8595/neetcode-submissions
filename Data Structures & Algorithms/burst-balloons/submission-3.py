class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # pick any ballon = find non burst ballon on left & right = vis, if left or right IND present or not, else while -1  or while +1
        # not pick = move to other ballon

        # this is not pick npick problen, it is partition dp
        # similar to MCM, but in reverse it will be solved
        # by reverse, i mean - select which ballon will be last poped, because, last ballon pop has 1, 1 left and right
        # if we pop that balloon that means, my left will have current as right, and right will have current as left

        INF = 10 ** 8
        n = len(nums)
        nums1 = [1] + nums + [1]

        def dfs(i, j):
            if i > j:
                return 0

            cost = -INF
            for k in range(i, j+1):
                ncost = nums1[i-1] * nums1[k] * nums1[j+1]
                ncost += dfs(i, k-1) + dfs(k+1, j)
                cost = max(cost, ncost)
            return cost

        # return dfs(1, n)

        dp = [[0 for j in range(n+2)] for i in range(n+2)]
        for i in range(n, 0, -1):
            for j in range(i, n+1):
                cost = -INF
                for k in range(i, j+1):
                    ncost = nums1[i-1] * nums1[k] * nums1[j+1]
                    ncost += dp[i][k-1] + dp[k+1][j]
                    cost = max(cost, ncost)
                dp[i][j] = cost
        return dp[1][n]
                