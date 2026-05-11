class Solution {
    public List<List<Integer>> subsets(int[] nums) {

        List<List<Integer>> ans = new ArrayList<>();

        int totalSubsets = (int) Math.pow(2, nums.length);

        for (int i = 0; i < totalSubsets; i++) {
            System.out.println(i);
            int mask = i;
            List<Integer> currSubset = new ArrayList<>();

            int j = 0;
            while (mask > 0 && j < nums.length) {
                if ((mask & 1) == 1) {
                    currSubset.add(nums[j]);
                }
                mask = mask >> 1;
                j++;
            }

            ans.add(currSubset);
        }
        return ans;
    }
}
