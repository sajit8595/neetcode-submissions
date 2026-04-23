class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        leftt = [-1] * n
        right = [-1] * n

        leftt[0] = 0
        for i in range(1, n):
            if height[leftt[i-1]] > height[i]:
                leftt[i] = leftt[i-1]
            else:
                leftt[i] = i
        
        right[n-1] = n-1
        for i in range(n-2, -1, -1):
            if height[right[i+1]] > height[i]:
                right[i] = right[i+1]
            else:
                right[i] = i
            
        ans = 0
        for i in range(n):
            currH = height[i]
            lefttH = height[leftt[i-1]] if i-1 >= 0 else currH
            rightH = height[right[i+1]] if i+1 < n else currH
            minH = min(lefttH, rightH)
            if minH > currH:
                ans += (minH - currH)
        return ans