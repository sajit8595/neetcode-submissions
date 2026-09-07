class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot & 1:
            return False
        
        tar = tot // 2

        n = len(nums)
        memo = {}
        def recur(ind, tar):
            if tar == 0:
                return True
            if tar < 0 or ind >= n:
                return False
            
            key = (ind, tar)
            if key in memo:
                return memo[key]

            take = recur(ind+1, tar - nums[ind])
            ntake = recur(ind+1, tar)
            memo[key] = take or ntake
            return memo[key]
        
        return recur(0, tar)