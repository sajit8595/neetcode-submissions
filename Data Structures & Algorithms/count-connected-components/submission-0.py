class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for i in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        vis = set()
        def dfs(node):
            vis.add(node)
            for child in adj[node]:
                if child not in vis:
                    dfs(child)
        
        ans = 0
        for i in range(n):
            if i not in vis:
                dfs(i)
                ans += 1
        return ans