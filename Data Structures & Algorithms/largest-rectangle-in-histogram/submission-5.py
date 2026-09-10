class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        n = len(heights)
        maxArea = 0

        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                currH = heights[st.pop()]
                left = st[-1] if st else -1
                right = i
                currArea = currH * (right - left - 1)
                maxArea = max(maxArea, currArea)
            st.append(i)
        
        while st:
            currH = heights[st.pop()]
            left = st[-1] if st else -1
            right = n 
            currArea = currH * (right - left - 1)
            maxArea = max(maxArea, currArea)

        return maxArea
