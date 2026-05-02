class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def minCoins(ind, amo):
            if ind == 0:
                if amo % coins[ind] == 0:
                    return amo // coins[ind]
                return float('inf')
            dontTake = minCoins(ind-1, amo)
            take = float('inf')
            if amo >= coins[ind]:
                take = 1 + minCoins(ind, amo-coins[ind])
            return min(dontTake, take)
        
        n = len(coins)
        # ans = minCoins(n-1, amount)
        # if ans == float('inf'):
        #     return -1
        # return ans

        dp = [[float('inf') for amo in range(amount+1)] for ind in range(n)]
        ind = 0
        for amo in range(amount+1):
            if amo % coins[ind] == 0:
                dp[ind][amo] = amo // coins[ind]
        
        for ind in range(1, n):
            for amo in range(amount+1):
                dontTake = dp[ind-1][amo]
                take = float('inf')
                if amo >= coins[ind]:
                    take = 1 + dp[ind][amo-coins[ind]]
                dp[ind][amo] = min(take, dontTake)

        if dp[n-1][amount] == float('inf'):
            return -1
        return dp[n-1][amount]
        