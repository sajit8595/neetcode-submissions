# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(root):
            if not root:
                ans.append('N')
                return
            ans.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ans = data.split(',')
        n = len(data)
        print(data, ans)
        ind = [0]
        def construct():
            if ind[0] == n:
                return None
            if ans[ind[0]] == 'N':
                ind[0] += 1
                return None
            node = TreeNode(int(ans[ind[0]]))
            ind[0] += 1
            node.left = construct()
            node.right = construct()
            return node
        
        return construct()