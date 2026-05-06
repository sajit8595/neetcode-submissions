class Solution {
    public int trap(int[] height) {
        int ans = 0;

        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < height.length; i++) {
            while (!st.isEmpty() && height[st.peek()] < height[i]) {
                int ind = height[st.pop()];
                if (!st.isEmpty()) {
                    int left = st.isEmpty() ? 0 : height[st.peek()];
                    int right = height[i];
                    int h = Math.min(left, right) - ind;
                    int w = i - st.peek() - 1;
                    ans += (h * w);
                }
            }
            st.push(i);
        }
        return ans;
    }
}
