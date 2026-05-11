class Solution {
    public List<List<Integer>> permute(int[] nums) {
        int n = nums.length;
        List<List<Integer>> ans = new ArrayList<>();
        boolean[] used = new boolean[n];
        backtrack(ans, nums, new ArrayList<>(), used, n);
        return ans;
    }

    public void backtrack(List<List<Integer>> ans, int[] nums, List<Integer> currAns, boolean[] used, int size) {
        if (currAns.size() == size) {
            ans.add(new ArrayList<>(currAns));
        } else {
            for (int i = 0; i < size; i++) {
                if (used[i] == false) {
                    currAns.add(nums[i]);
                    used[i] = true;
                    backtrack(ans, nums, currAns, used, size);
                    currAns.remove(currAns.size() - 1);
                    used[i] = false;
                }
            }
        }
    }
}
