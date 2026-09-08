class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # only one component
        # no cycles
        # edges = n-1

        if len(edges) != n-1:
            return False
        
        adj = [[] for i in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        vis = [0 for i in range(n)]
        def dfs_cycle_check(node, par):
            vis[node] = 1
            for child in adj[node]:
                if vis[child] == 0:
                    if (dfs_cycle_check(child, node)):
                        return True
                elif child != par:
                    return True
            return False
        
        isCycle = dfs_cycle_check(0, -1)
        
        if isCycle:
            return False
        
        for i in range(n):
            if vis[i] == 0:
                return False
        
        return True