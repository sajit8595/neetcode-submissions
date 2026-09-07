# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(root):
            if not root:
                return [True, 0]
            isBL, hL = recur(root.left)
            if not isBL:
                return [isBL, hL]

            isBR, hR = recur(root.right)
            if not isBR:
                return [isBR, hR]

            return [abs(hL - hR) <= 1, 1 + max(hL, hR)]
        
        balance, _ = recur(root)
        return balance
