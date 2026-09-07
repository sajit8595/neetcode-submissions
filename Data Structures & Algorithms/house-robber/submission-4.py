class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        n = len(nums)
        def recur(ind):
            if ind >= n:
                return 0

            if ind in memo:
                return memo[ind]

            steal = nums[ind] + recur(ind+2)
            noSteal = 0 + recur(ind+1)
            memo[ind] = max(steal, noSteal)
            return memo[ind]

        return recur(0)