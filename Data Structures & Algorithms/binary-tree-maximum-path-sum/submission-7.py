# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = -float('inf')
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            right = recur(root.right)
            self.maxi = max(self.maxi, left + right + root.val, root.val, left + root.val, right + root.val)
            return max(root.val, root.val + max(left, right))
        recur(root)
        return self.maxi