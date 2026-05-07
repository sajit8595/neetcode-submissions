class Solution {
    public int findDuplicate(int[] nums) {
        // nums range (1, n), size = n+1
        // head = ind; next = nums[ind];
        int size = nums.length;
        int slow = 0;
        int fast = 0;

        while (true) {
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (slow == fast) {
                fast = 0;
                while (true) {
                    slow = nums[slow];
                    fast = nums[fast];
                    if (slow == fast) {
                        return slow;
                    }
                }
            }
        }
    }
}
