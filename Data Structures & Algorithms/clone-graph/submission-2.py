"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        memo = {}
        def clone(node):
            if not node:
                return None
                
            if node.val not in memo:
                newNode = Node(node.val)
                memo[node.val] = newNode
                for neigh in node.neighbors:
                    newNode.neighbors.append(clone(neigh))

            return memo[node.val]
        
        return clone(node)
                