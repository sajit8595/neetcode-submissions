# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(left, root, right):
            if not root:
                return True
            if left >= root.val or right <= root.val:
                return False
            v1 = isValid(left, root.left, root.val)
            v2 = isValid(root.val, root.right, right)
            return v1 and v2

        return isValid(-float('inf'), root, float('inf'))