# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            right = recur(root.right)
            dia = left + right
            # print(root.val, left, right, dia)
            self.maxi = max(self.maxi, dia)
            return 1 + max(left, right)
        recur(root)
        return self.maxi
