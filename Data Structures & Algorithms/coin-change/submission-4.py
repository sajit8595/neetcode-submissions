class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        memo = {}
        def few(ind, amount):
            if amount == 0:
                return 0
            if ind >= n or amount < 0:
                return float('inf')
            
            key = (ind, amount)
            if key in memo:
                return memo[key]

            take = 1 + few(ind, amount - coins[ind])
            ntake = 0 + few(ind+1, amount)
            memo[key] = min(take, ntake)
            return memo[key]
        
        ans = few(0, amount)
        if ans == float('inf'):
            return -1
        return ans