class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # come from back, greedy, if i can reach end
        n = len(nums)
        end = n-1
        
        for ind in range(n-2, -1, -1):
            dist = ind + nums[ind]
            if dist >= end:
                end = ind

        return end == 0