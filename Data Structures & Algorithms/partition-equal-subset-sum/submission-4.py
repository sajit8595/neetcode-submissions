class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        summ = sum(nums)
        if summ & 1:
            return False
        target = summ // 2

        # def achieve(ind, tar):
        #     if tar == 0:
        #         return True
        #     if ind == 0:
        #         return tar == nums[ind]

        #     dontTake = achieve(ind-1, tar)
        #     take = False
        #     if tar >= nums[ind]:
        #         take = achieve(ind-1, tar-nums[ind])
        #     return dontTake or take

        # return achieve(n-1, target)

        dp = [[False for t in range(target+1)] for ind in range(n)]

        tar = 0
        for ind in range(n):
            dp[ind][tar] = True
        ind = 0
        if nums[ind] <= tar:
            dp[ind][nums[ind]] = True

        for ind in range(1, n):
            for tar in range(1, target+1):
                dontTake = dp[ind-1][tar]
                take = False
                if tar >= nums[ind]:
                    take = dp[ind-1][tar-nums[ind]]
                dp[ind][tar] = dontTake or take
        return dp[n-1][target]
        
