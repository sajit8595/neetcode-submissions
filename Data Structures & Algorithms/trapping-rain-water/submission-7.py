class Solution:
    def trap(self, height: List[int]) -> int:
        # find left max, right max - take min of them
        # subtract currH = curr tile saved water

        lm, rm = 0, 0
        ans = 0
        n = len(height)

        l, r  = 0, n-1
        while l <= r:
            if height[l] < height[r]:
                lm = max(lm, height[l])
                ans += lm - height[l]
                l += 1
            else:
                rm = max(rm, height[r])
                ans += rm - height[r]
                r -= 1
        return ans