class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        low = 0
        high = n-1

        while low <= high:
            if heights[low] < heights[high]:
                newAns = heights[low] * (high - low)
                low += 1
            else:
                newAns = heights[high] * (high - low)
                high -= 1
            ans = max(ans, newAns)
            
        return ans