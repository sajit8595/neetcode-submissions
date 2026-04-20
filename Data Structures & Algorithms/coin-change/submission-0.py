class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf') for target in range(amount+1)] for ind in range(n)]

        for ind in range(n):
            dp[ind][0] = 0

        for target in range(amount+1):
            if target % coins[0] == 0:
                dp[0][target] = target // coins[0]
        
        for ind in range(1, n):
            for target in range(amount+1):
                consider = notConsider = float('inf')
                if target >= coins[ind]:
                    consider = 1 + dp[ind][target-coins[ind]]
                notConsider = 0 + dp[ind-1][target]
                dp[ind][target] = min(consider, notConsider)

        ans = dp[n-1][amount]
        if ans == float('inf'):
            return -1
        return ans

        def recur(ind, target):
            if target == 0:
                return 0
            if ind == 0:
                if target % coins[0] == 0:
                    return target // coins[0]
                return float('inf')

            consider = notConsider = float('inf')
            if target >= coins[ind]:
                consider = 1 + recur(ind, target-coins[ind])
            notConsider = 0 + recur(ind-1, target)
            return min(consider, notConsider)
        
        ans = recur(n-1, amount)
        if ans == float('inf'):
            return -1
        return ans