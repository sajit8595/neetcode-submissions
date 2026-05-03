class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # def minCost(ind):
        #     if ind >= n:
        #         return 0
        #     return cost[ind] + min(minCost(ind+1), minCost(ind+2))
        # # return min(minCost(0), minCost(1))

        prev1 = prev2 = 0
        for c in range(n-1, -1, -1):
            newCost = cost[c] + min(prev1, prev2)
            prev2 = prev1
            prev1 = newCost

        return min(prev1, prev2)