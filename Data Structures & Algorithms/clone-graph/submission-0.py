"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        vis = {}
        def clone(node):
            if not node:
                return None
            newNode = Node(node.val)
            vis[node.val] = newNode
            for neigh in node.neighbors:
                if neigh.val not in vis:
                    cloneNeigh = clone(neigh)
                else:
                    cloneNeigh = vis[neigh.val]
                newNode.neighbors.append(cloneNeigh)
            return newNode
        
        return clone(node)