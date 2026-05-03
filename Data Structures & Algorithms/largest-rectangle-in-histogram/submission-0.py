class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        ans = 0
        n = len(heights)
        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                height = heights[st.pop()]
                left = st[-1] if st else -1
                right = i
                area = height * (right - left - 1)
                ans = max(ans, area)
            st.append(i)
        
        while st:
            height = heights[st.pop()]
            left = st[-1] if st else -1
            right = n
            area = height * (right - left - 1)
            ans = max(ans, area)
        return ans