# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [-float('inf')]
        def maxSum(root):
            if not root:
                return 0
            leftSum = max(maxSum(root.left), 0)
            rightSum = max(maxSum(root.right), 0)
            ans[0] = max(ans[0], leftSum + rightSum + root.val)
            return root.val + max(leftSum, rightSum)

        maxSum(root)
        return ans[0]