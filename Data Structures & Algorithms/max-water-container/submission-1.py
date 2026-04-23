class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        l, r = 0, n-1
        while l < r:
            base = r - l
            if heights[l] < heights[r]:
                height = heights[l]
                l += 1
            else:
                height = heights[r]
                r -= 1
            ans = max(ans, base * height)
        return ans