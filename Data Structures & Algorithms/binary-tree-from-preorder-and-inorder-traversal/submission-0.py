# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def binarySearch(l, r, tar):
            # binary Search cannot be applied, as it is not a BST, it is BT
            for x in range(l, r+1):
                if inorder[x] == tar:
                    return x 

        def build(ps, pe, ins, ine):
            if ps > pe or ins > ine:
                return None
            root = TreeNode(preorder[ps])
            rootInd = binarySearch(ins, ine, preorder[ps])
            noEles = rootInd - ins
            # noEles = ine - rootInd
            root.left = build(ps+1, ps+noEles, ins, ins+noEles-1)
            root.right = build(ps+noEles+1, pe, ins+noEles+1, ine)
            return root
        
        n = len(preorder)
        return build(0, n-1, 0, n-1)