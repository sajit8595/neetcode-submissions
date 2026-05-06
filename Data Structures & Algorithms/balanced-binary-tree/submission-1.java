
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    public int[] getHeight(TreeNode root) {
        if (root == null) {
            return new int[]{1,0};
        }
        int[] left = getHeight(root.left);
        int[] right = getHeight(root.right);

        int height = 1 + Math.max(left[1], right[1]);
        int balanced = 0;

        if (left[0] == 0 || right[0] == 0) {
            return new int[]{balanced, height};
        }
        
        if (Math.abs(left[1] - right[1]) <= 1) {
            balanced = 1;
        }
        return new int[]{balanced, height};   
    }

    public boolean isBalanced(TreeNode root) {
        return getHeight(root)[0] == 1;
    }
}
