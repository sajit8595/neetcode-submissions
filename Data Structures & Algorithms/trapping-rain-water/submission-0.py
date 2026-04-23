class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        leftt = [-1] * n
        right = [-1] * n

        for i in range(n):
            if i == 0:
                leftt[i] = 0
                continue
            if height[leftt[i-1]] > height[i]:
                leftt[i] = leftt[i-1]
            else:
                leftt[i] = i
        
        for i in range(n-1, -1, -1):
            if i == n-1:
                right[i] = n-1
                continue
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