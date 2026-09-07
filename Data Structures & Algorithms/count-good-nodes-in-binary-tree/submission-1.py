# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        def recur(root, maxi):
            if not root:
                return
            if root.val >= maxi:
                self.good += 1
                maxi = root.val
            recur(root.left, maxi)
            recur(root.right, maxi)
        recur(root, -float('inf'))
        return self.good