class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def recur(ind):
            if ind == n-1:
                return 0

            if nums[ind] == 0:
                return float('inf')

            if ind in memo:
                return memo[ind]

            ans = float('inf')
            minJump = min(ind + nums[ind] + 1, n)
            for xind in range(ind + 1, minJump):
                ans = min(ans, 1 + recur(xind))

            memo[ind] = ans
            return ans
        
        return recur(0)