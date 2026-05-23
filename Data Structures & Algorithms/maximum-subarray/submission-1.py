class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algo - checkout maxProductSubArray
        ans = nums[0]
        currAns = ans
        for i in range(1, len(nums)):
            currAns = max(currAns + nums[i], nums[i])
            ans = max(ans, currAns)
        return ans