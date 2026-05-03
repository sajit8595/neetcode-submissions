class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        ans = 0
        n = len(heights)

        def getArea(st, right):
            height = heights[st.pop()]
            left = st[-1] if st else -1
            return height * (right - left -1)

        for right in range(n):
            while st and heights[st[-1]] > heights[right]:
                ans = max(ans, getArea(st, right))
            st.append(right)
        
        while st:
            ans = max(ans, getArea(st, n))
        return ans