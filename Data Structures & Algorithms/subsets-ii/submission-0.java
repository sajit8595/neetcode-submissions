class Solution {

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        backtrack(ans, nums, new ArrayList<>(), 0);
        return ans;
    }

    public void backtrack(List<List<Integer>> ans, int[] nums, List<Integer> currAns, int start) {
        ans.add(new ArrayList<>(currAns));
        for (int ind = start; ind < nums.length; ind++) {
            if (ind > start && nums[ind-1] == nums[ind]) {
                continue;
            }
            currAns.add(nums[ind]);
            backtrack(ans, nums, currAns, ind+1);
            currAns.remove(currAns.size() - 1);
        }
    }
}
