class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree vs graph
        # tree has no cycles
        # tree is fully connected
        # exactly n-1 edges
        if len(edges) != n-1:
            return False
        
        adj = [[] for i in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        vis = set()
        def hasCycle(node, par):
            vis.add(node)
            for child in adj[node]:
                if child not in vis:
                    if hasCycle(child, node):
                        return True
                elif child != par:
                    return True
            return False
        
        return hasCycle(0, -1) == False and len(vis) == n