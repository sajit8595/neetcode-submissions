class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        def maxAnswer(i, j):
            p1, p2 = 0, 0
            for p in range(i, j):
                take = nums[p] + p1
                ntake = 0 + p2
                p1 = p2
                p2 = max(take, ntake)
            return p2

        ans1 = maxAnswer(0, n-1)
        ans2 = maxAnswer(1, n)
        return max(ans1, ans2)
        
            
