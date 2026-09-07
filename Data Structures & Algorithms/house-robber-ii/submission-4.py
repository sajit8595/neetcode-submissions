class Solution:
    def rob_noncircular(self, nums: List[int]) -> int:
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

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        way1 = self.rob_noncircular(nums[1:])
        way2 = self.rob_noncircular(nums[:-1])
        return max(way1, way2)