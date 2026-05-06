class Solution {
    public int largestRectangleArea(int[] heights) {
        int ans = 0;

        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < heights.length; i++) {
            while (!st.isEmpty() && heights[st.peek()] > heights[i]) {
                int currHeight = heights[st.pop()];
                int left = -1;
                if (!st.isEmpty()) {
                    left = st.peek();
                }
                int area = currHeight * (i - left - 1);
                ans = Math.max(ans, area);
            }
            st.push(i);
        }

        while (!st.isEmpty()) {
            int currHeight = heights[st.pop()];
            int left = -1;
            int i = heights.length;
            if (!st.isEmpty()) {
                left = st.peek();
            }
            int area = currHeight * (i - left - 1);
            ans = Math.max(ans, area);
        }

        return ans;
    }
}
