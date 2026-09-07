# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lvlOrder = []

        dq = deque([])
        if root:
            dq.append(root)
        while dq:
            n = len(dq)
            lvlOrder.append(dq[n-1].val)
            for _ in range(n):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return lvlOrder