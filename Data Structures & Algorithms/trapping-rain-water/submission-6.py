class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftt = [-1] * n
        right = [-1] * n

        leftt[0] = height[0]
        for i in range(1, n):
            leftt[i] = max(leftt[i-1], height[i])
        
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
            
        ans = 0
        for i in range(n):
            ans += (min(leftt[i], right[i]) - height[i])
        return ans