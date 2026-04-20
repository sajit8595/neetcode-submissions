class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # brute force
        maxAns = max(nums)
        n = len(nums)

        for i in range(n):
            currMax = nums[i]
            for j in range(i+1, n):
                currMax *= nums[j]
                maxAns = max(maxAns, currMax)
        return maxAns