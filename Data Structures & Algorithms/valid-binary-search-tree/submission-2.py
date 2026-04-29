# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, l, r):
            if not root:
                return True
            if l < root.val < r:
                return isValid(root.left, l, root.val) and isValid(root.right, root.val, r)
            return False
        
        return isValid(root, -float('inf'), float('inf'))