class Solution {
    public int trap(int[] height) {
        int ans = 0;

        int l = 0; int r = height.length-1;
        int leftMax = 0;
        int rightMax = 0;

        while (l <= r) {
            if (leftMax < rightMax) {
                leftMax = Math.max(leftMax, height[l]);
                ans += (leftMax - height[l]);
                l++;
            } else {
                rightMax = Math.max(rightMax, height[r]);
                ans += (rightMax - height[r]);
                r--;
            }
        }

        return ans;
    }
}
