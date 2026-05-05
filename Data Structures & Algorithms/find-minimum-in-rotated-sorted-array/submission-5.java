
class Solution {
    public int findMin(int[] nums) {

        int low = 0;
        int high = nums.length-1;

        int ans = nums[0];

        while (low <= high) {
            int mid = (low + high) / 2;
            ans = Math.min(ans, nums[mid]);
            if (nums[mid] < nums[high]) {
                high = mid-1;
            } else {
                low = mid+1;
            }
        }
        return ans;
    }
}
