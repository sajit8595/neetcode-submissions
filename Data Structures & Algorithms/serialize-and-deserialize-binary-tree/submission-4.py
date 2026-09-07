# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        seri = []
        def dfs(root):
            if not root:
                seri.append('N')
                return
            seri.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(seri)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arrData = data.split(',')
        self.it = 0
        def deseri():
            dataVal = arrData[self.it]
            self.it += 1
            if dataVal == 'N':
                return None
                
            node = TreeNode(int(dataVal))
            node.left = deseri()
            node.right = deseri()
            return node
        return deseri()