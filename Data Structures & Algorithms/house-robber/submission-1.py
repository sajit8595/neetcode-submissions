class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        p1 = nums[0]
        p2 = max(nums[0], nums[1])
        
        for p in range(2, n):
            take = nums[p] + p1
            ntake = 0 + p2
            p1 = p2
            p2 = max(take, ntake)
        return p2

        # def recur(ind):
        #     if ind < 0:
        #         return 0
        #     take = nums[ind] + recur(ind-2)
        #     ntake = 0 + recur(ind-1)
        #     return max(take, ntake)
        
        # return recur(len(nums)-1)