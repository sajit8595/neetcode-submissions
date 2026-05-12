class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def recur(ind, amount):
            if amount == 0:
                return 1
            if ind == 0:
                if amount % coins[0] == 0:
                    return 1
                return 0

            key = (ind, amount)
            if key in memo:
                return memo[key]
            # takeCoin if feasiable
            take = 0
            if coins[ind] <= amount:
                take = recur(ind, amount - coins[ind])
            # dontTakeCoin
            dtake = recur(ind-1, amount)
            memo[key] = dtake + take
            return memo[key]
        
        return recur(len(coins)-1, amount)