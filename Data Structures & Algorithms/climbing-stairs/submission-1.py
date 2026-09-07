class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def recur(ind):
            if ind == 1:
                return 1
            if ind == 2:
                return 2
            if ind in memo:
                return memo[ind]
            memo[ind] = recur(ind-1) + recur(ind-2)
            return memo[ind]
        return recur(n)