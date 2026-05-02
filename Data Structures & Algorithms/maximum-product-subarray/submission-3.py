class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        currMin = currMax = 1
        for i in range(len(nums)):
            maxMul = currMax * nums[i]
            minMul = currMin * nums[i]
            currMax = max(nums[i], maxMul, minMul)
            currMin = min(nums[i], maxMul, minMul)
            ans = max(ans, currMax, currMin)
        return ans