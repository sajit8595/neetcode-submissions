# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # st = []
        # while st or root:
        #     while root:
        #         st.append(root)
        #         root = root.left
        #     x = st.pop()
        #     k -= 1
        #     if k == 0:
        #         return x.val
        #     root = x.right
        
        # inorder traversal - morris - left, root, right
        
        # ans = []
        curr = root
        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                # ans.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                
                if pre.right == curr:
                    k -= 1
                    if k == 0:
                        return curr.val
                    pre.right = None
                    curr = curr.right
                else:
                    # ans.append(curr.val)
                    pre.right = curr
                    curr = curr.left
        # print(ans)
        return -1