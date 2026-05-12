class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def recur(ind, target):
            if ind < 0:
                if target == 0:
                    return 1
                return 0
            key = (ind, target)
            if key in memo:
                return memo[key]
            # add
            add = recur(ind-1, target+nums[ind])
            sub = recur(ind-1, target-nums[ind])
            memo[key] = add + sub
            return memo[key]
        
        return recur(len(nums)-1, target)