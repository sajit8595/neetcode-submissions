# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return same(p.left, q.left) and same(p.right, q.right)
        
        def issub(a, b):
            if not a:
                return False
            
            if a.val == b.val:
                if same(a, b):
                    return True
                    
            return issub(a.left, b) or issub(a.right, b)
        
        return issub(root, subRoot)