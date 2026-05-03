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

        pdp = [False for t in range(target+1)]
        tar = 0; pdp[tar] = True
        ind = 0
        if nums[ind] <= tar:
            pdp[nums[ind]] = True

        for ind in range(1, n):
            curr = pdp[:]
            for tar in range(1, target+1):
                dontTake = pdp[tar]
                take = False
                if tar >= nums[ind]:
                    take = pdp[tar-nums[ind]]
                curr[tar] = dontTake or take
            pdp = curr
        return pdp[target]
        
