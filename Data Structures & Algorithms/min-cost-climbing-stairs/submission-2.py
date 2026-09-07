class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        n = len(cost)
        def recur(ind):
            if ind >= n:
                return 0

            if ind in memo:
                return memo[ind]

            j1 = recur(ind+1)
            j2 = recur(ind+2)
            memo[ind] = cost[ind] + min(j1, j2)
            return memo[ind]
        
        return min(recur(0), recur(1))