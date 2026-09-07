# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recur(root):
            if not root:
                return None
            if root.val == p.val or root.val == q.val:
                return root
            left = recur(root.left)
            right = recur(root.right)
            if left and right:
                return root
            return left or right
        return recur(root)