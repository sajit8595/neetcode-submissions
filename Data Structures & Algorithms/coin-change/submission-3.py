class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        prev = [float('inf') for amo in range(amount+1)]
        ind = 0
        for amo in range(amount+1):
            if amo % coins[ind] == 0:
                prev[amo] = amo // coins[ind]
        
        for ind in range(1, n):
            curr = [float('inf') for amo in range(amount+1)]
            for amo in range(amount+1):
                dontTake = prev[amo]
                take = float('inf')
                if amo >= coins[ind]:
                    take = 1 + curr[amo-coins[ind]]
                curr[amo] = min(take, dontTake)
            prev = curr

        if prev[amount] == float('inf'):
            return -1
        return prev[amount]
        