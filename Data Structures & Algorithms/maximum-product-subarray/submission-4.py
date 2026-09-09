class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minP, maxP = 1, 1
        maxV = -float('inf')

        for n in nums:
            newMinP = minP * n
            newMaxP = maxP * n
            minP = min(n, newMinP, newMaxP)
            maxP = max(n, newMinP, newMaxP)
            maxV = max(maxV, minP, maxP)

        return maxV