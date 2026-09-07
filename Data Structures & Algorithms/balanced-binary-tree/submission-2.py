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
            isBR, hR = recur(root.right)
            isBalance = abs(hL - hR) <= 1
            maxH = 1 + max(hL, hR)
            return [isBL and isBR and isBalance, maxH]
        
        balance, _ = recur(root)
        return balance
